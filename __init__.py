import bpy # type: ignore

bl_info = {
    "name": "Merle Custom Addons",
    "author": "mkrzywdz",
    "version": (0, 1, 1),
    "blender": (5, 2, 0),
    "category": "3D View",
}

from .panels.main_panel import CUSTOMADDON_PT_main
from .panels.wheat_panel import (
    CUSTOMADDON_PT_wheat_collection,
    CUSTOMADDON_PT_wheat_create,
    VIEW3D_MT_merle_wheat,
)
from .operators.wheat_operator import (
    CUSTOMADDON_OT_wheat_collection,
    CUSTOMADDON_OT_wheat_create,
)
from .properties.wheat_properties import WheatProperties

from .panels.thunders_panel import (
    CUSTOMADDON_PT_thunderball,
    VIEW3D_MT_merle_thunders,
)
from .operators.thunderball_operator import (
    CUSTOMADDON_OT_thunderball_create,
)
from .properties.thunders_properties import ThundersProperties


def menu_func(self, context):
    self.layout.menu(
        VIEW3D_MT_merle_add.bl_idname,
        icon='PLUGIN'
    )

class VIEW3D_MT_merle_add(bpy.types.Menu):
    bl_idname = "VIEW3D_MT_merle_add"
    bl_label = "Merle Custom Addons"

    def draw(self, context):
        layout = self.layout

        layout.menu(
            VIEW3D_MT_merle_wheat.bl_idname,
            icon='CURVE_DATA'
        )

        layout.menu(
            VIEW3D_MT_merle_thunders.bl_idname,
            icon='FORCE_VORTEX'
        )

classes = (
    CUSTOMADDON_PT_main,
    CUSTOMADDON_PT_wheat_create,
    CUSTOMADDON_PT_wheat_collection,
    CUSTOMADDON_OT_wheat_collection,
    CUSTOMADDON_OT_wheat_create,
    WheatProperties,
    CUSTOMADDON_PT_thunderball,
    CUSTOMADDON_OT_thunderball_create,
    ThundersProperties,
    VIEW3D_MT_merle_add,
    VIEW3D_MT_merle_wheat,
    VIEW3D_MT_merle_thunders
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.wheat_props = bpy.props.PointerProperty(
        type=WheatProperties
    )

    bpy.types.Scene.thunders_props = bpy.props.PointerProperty(
        type=ThundersProperties
    )

    bpy.types.VIEW3D_MT_add.append(
        menu_func
    )

def unregister():
    bpy.types.VIEW3D_MT_add.remove(
        menu_func
    )

    del bpy.types.Scene.wheat_props
    del bpy.types.Scene.thunders_props

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)