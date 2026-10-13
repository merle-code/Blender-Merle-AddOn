import bpy

bl_info = {
    "name": "Custom Addon",
    "author": "mkrzywdz",
    "version": (0, 1, 0),
    "blender": (5, 2, 0),
    "category": "3D View",
}

class CUSTOMADDON_PT_main(bpy.types.Panel):
    bl_label = "Custom Addon"
    bl_idname = "CUSTOMADDON_PT_main"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Custom"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Hello World")


def register():
    bpy.utils.register_class(CUSTOMADDON_PT_main)


def unregister():
    bpy.utils.unregister_class(CUSTOMADDON_PT_main)