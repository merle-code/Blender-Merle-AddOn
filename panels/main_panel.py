import bpy # type: ignore

class MCA_PT_main(bpy.types.Panel):
    bl_label = "Custom Addon"
    bl_idname = "MCA_PT_main"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Custom"

    def draw(self, context):
        layout = self.layout
