import bpy # type: ignore

from .. import bl_info

class VIEW3D_MT_merle_thunders(bpy.types.Menu):
    bl_idname = "VIEW3D_MT_merle_thunders"
    bl_label = "Thunders"

    def draw(self, context):
        layout = self.layout

        layout.operator(
            "customaddon.thunderball_create",
            text="ThunderBall",
            icon='SPHERE'
        )


class MCA_PT_thunderball(bpy.types.Panel):
    bl_label = "Thunders"
    bl_idname = "MCA_PT_thunderball"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Custom"
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = "MCA_PT_main"
    bl_order = 20

    def draw(self, context):

        layout = self.layout

        props = context.scene.thunders_props

        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.prop(props, "base_name")
        layout.prop(props, "seed")

        layout.prop(props, "convert_to_mesh")

        layout.operator(
            "customaddon.thunderball_create",
            text="Create"
        )