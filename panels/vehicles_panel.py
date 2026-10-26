import bpy # type: ignore
from pathlib import Path
from ..config import vehicles

from ..utils.blender_assets import get_assets_dir
from ..utils.blender_icons import (
    get_icon_id,
)

def get_vehicle_names():
    vehicles_dir = (
        get_assets_dir()
        / vehicles.BLEND_DIR_NAME
    )
    print(f"vehicles_dir: {vehicles_dir}")
    return sorted(
        [
            file.stem
            for file in vehicles_dir.glob("*.blend")
        ]
    )


class VIEW3D_MT_merle_vehicles(bpy.types.Menu):
    bl_idname = "VIEW3D_MT_merle_vehicles"
    bl_label = vehicles.MENU_GROUP_NAME

    def draw(self, context):

        layout = self.layout

        for vehicle_name in get_vehicle_names():
            icon_id = get_icon_id(vehicle_name)

            if icon_id:
                op = layout.operator(
                    "customaddon.vehicle_add",
                    text=vehicle_name,
                    icon_value=icon_id
                )
            else:
                op = layout.operator(
                    "customaddon.vehicle_add",
                    text=vehicle_name,
                    icon=vehicles.DEFAULT_ITEM_ICON
                )

            op.vehicle_name = vehicle_name