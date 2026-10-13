import bpy


class CUSTOMADDON_PT_thunderball(bpy.types.Panel):
    bl_label = "ThunderBall"
    bl_idname = "CUSTOMADDON_PT_thunderball"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Custom"
    bl_options = {'DEFAULT_CLOSED'}
    bl_parent_id = "CUSTOMADDON_PT_main"
    bl_order = 20

    def draw(self, context):
        layout = self.layout
        layout.label(text="ThunderBall")