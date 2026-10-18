import bpy # type: ignore

from .. import bl_info

def draw_wheat_menu(layout, context):

    layout.menu(
        "VIEW3D_MT_merle_wheat",
        icon='CURVE_DATA'
    )

class VIEW3D_MT_merle_wheat(bpy.types.Menu):
    bl_idname = "VIEW3D_MT_merle_wheat"
    bl_label = "Wheats"

    def draw(self, context):
        layout = self.layout

        layout.operator(
            "customaddon.wheat_create",
            text="Wheat",
            icon='CURVE_DATA'
        ).convert_to_mesh = False

        layout.operator(
            "customaddon.wheat_create",
            text="Wheat (Mesh)",
            icon='MESH_DATA'
        ).convert_to_mesh = True

class CUSTOMADDON_PT_wheat_create(bpy.types.Panel):
    bl_label = "Wheat Create"
    bl_idname = "CUSTOMADDON_PT_wheat_create"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Custom"
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = "CUSTOMADDON_PT_main"
    bl_order = 5

    def draw(self, context):

        layout = self.layout

        props = context.scene.wheat_props

        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.prop(props, "base_name")
        layout.prop(props, "seed")
        layout.prop(props, "convert_to_mesh")

        layout.operator(
            "customaddon.wheat_create",
            text="Create"
        )

class CUSTOMADDON_PT_wheat_collection(bpy.types.Panel):
    bl_label = "Wheat Collection Generator"
    bl_idname = "CUSTOMADDON_PT_wheat_collection"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Custom"
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = "CUSTOMADDON_PT_main"
    bl_order = 10

    def draw(self, context):

        layout = self.layout

        props = context.scene.wheat_props

        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.prop(props, "base_name")
        layout.prop(props, "count")
        layout.prop(props, "collection_name")
        layout.prop(props, "seed_start")

        row = layout.row(align=True)

        row.prop(props, "density")
        row.prop(props, "jitter")

        layout.operator(
            "customaddon.wheat_collection",
            text="Generate"
        )