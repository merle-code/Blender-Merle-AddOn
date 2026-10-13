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
    VIEW3D_MT_merle_add,
    menu_func,
)
from .panels.thunderball_panel import CUSTOMADDON_PT_thunderball

from .operators.wheat_operator import (
    CUSTOMADDON_OT_wheat_collection,
    CUSTOMADDON_OT_wheat_create,
)

from .properties.wheat_properties import WheatProperties

classes = (
    CUSTOMADDON_PT_main,
    CUSTOMADDON_PT_wheat_create,
    CUSTOMADDON_PT_wheat_collection,
    CUSTOMADDON_PT_thunderball,
    CUSTOMADDON_OT_wheat_collection,
    CUSTOMADDON_OT_wheat_create,
    VIEW3D_MT_merle_add,
    WheatProperties,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.wheat_props = bpy.props.PointerProperty(
        type=WheatProperties
    )

    bpy.types.VIEW3D_MT_add.append(menu_func)


def unregister():
    bpy.types.VIEW3D_MT_add.remove(menu_func)

    del bpy.types.Scene.wheat_props

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)