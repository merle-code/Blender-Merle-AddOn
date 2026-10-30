import bpy # type: ignore

import math, random

from ..utils.validators import validate_wheat_properties
from ..utils.blender_collections import (
    create_collection,
)
from ..utils.blender_wheat_assets import (
    get_wheat_node_group,
)
from ..utils.blender_wheat_objects import (
    create_wheat,
)
from ..utils.blender_objects import (
    duplicate_object,
    convert_to_mesh,
    remove_empty_material_slots,
    delete_object,
)

from ..utils.blender_gn import (
    set_gn_input,
)

GOLDEN_ANGLE = math.radians(137.507764)

class MCA_OT_wheat_create(bpy.types.Operator):
    bl_idname = "customaddon.wheat_create"
    bl_label = "Create Wheat"

    convert_to_mesh: bpy.props.BoolProperty(
        default=False
    ) # type: ignore

    def execute(self, context):

        props = context.scene.wheat_props
        
        error = validate_wheat_properties(props)

        if error:
            self.report({'ERROR'}, error)
            return {'CANCELLED'}
        
        node_group = get_wheat_node_group()

        if not node_group: return {'CANCELLED'}
        
        wheat = create_wheat(
            node_group
        )
        set_gn_input(wheat, "Seed", props.seed + 1)
        set_gn_input(wheat, "ID", props.seed + 1)

        if props.convert_to_mesh or self.convert_to_mesh:
            convert_to_mesh(wheat)
            remove_empty_material_slots(wheat)
        return {'FINISHED'}


class MCA_OT_wheat_collection(bpy.types.Operator):
    bl_idname = "customaddon.wheat_collection"
    bl_label = "Generate Wheat"

    def execute(self, context):

        props = context.scene.wheat_props

        error = validate_wheat_properties(props)

        if error:
            self.report({'ERROR'}, error)
            return {'CANCELLED'}

        collection = create_collection(
            props.collection_name
        )
        node_group = get_wheat_node_group()

        source = create_wheat(
            node_group
        )

        for i in range(props.count):
            copy = duplicate_object(source)
            collection.objects.link(copy)
            copy.name = f"{props.base_name}_{i:03d}"

            r = props.density * math.sqrt(i)
            angle = i * GOLDEN_ANGLE

            locationX = r * math.cos(angle)
            locationY = r * math.sin(angle)
            if props.jitter:
                jitter = props.density * 0.01
                locationX += random.uniform(-jitter, jitter)
                locationY += random.uniform(-jitter, jitter)

            copy.location = (
                locationX,
                locationY,
                0
            )

            set_gn_input(copy, "Seed", i + 1)
            set_gn_input(copy, "ID", i)
            convert_to_mesh(copy)
            remove_empty_material_slots(copy)

        delete_object(source)

        self.report(
            {'INFO'},
            f"Created: {props.collection_name}"
        )

        return {'FINISHED'}