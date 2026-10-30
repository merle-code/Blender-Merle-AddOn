import bpy # type: ignore

from ..utils.validators import validate_thunders_properties

from ..utils.blender_thunders_assets import (
    get_thunderball_node_group,
)
from ..utils.blender_thunders_objects import (
    create_thunderball,
)
from ..utils.blender_objects import (
    convert_to_mesh,
    remove_empty_material_slots,
)

from ..utils.blender_gn import (
    set_gn_input,
)

class MCA_OT_thunderball_create(bpy.types.Operator):
    bl_idname = "customaddon.thunderball_create"
    bl_label = "Create ThunderBall"

    convert_to_mesh: bpy.props.BoolProperty(
        default=False
    ) # type: ignore

    def execute(self, context):

        props = context.scene.thunders_props
        
        error = validate_thunders_properties(props)

        if error:
            self.report({'ERROR'}, error)
            return {'CANCELLED'}
        
        node_group = get_thunderball_node_group()

        if not node_group: return {'CANCELLED'}
        
        thunderball = create_thunderball(
            node_group
        )
        set_gn_input(thunderball, "Seed", props.seed + 1)


        if props.convert_to_mesh or self.convert_to_mesh:
            convert_to_mesh(thunderball)
            remove_empty_material_slots(thunderball)
        return {'FINISHED'}

