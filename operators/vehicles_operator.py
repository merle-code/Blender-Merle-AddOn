import bpy # type: ignore
from pathlib import Path

from ..config import vehicles

class MCA_OT_vehicle_add(bpy.types.Operator):
    bl_idname = "customaddon.vehicle_add"
    bl_label = "Add Vehicle"

    vehicle_name: bpy.props.StringProperty() # type: ignore

    def execute(self, context):

        print(
            f"Add vehicle: "
            f"{self.vehicle_name}"
        )

        addon_dir = Path(__file__).parent.parent

        blend_file = (
            addon_dir
            / "assets"
            / vehicles.BLEND_DIR_NAME
            / f"{self.vehicle_name}.blend"
        )

        collection_name = self.vehicle_name

        objects_dir = str(
            blend_file / "Collection"
        )

        try:

            bpy.ops.wm.append(
                filepath=str(
                    blend_file
                    / "Collection"
                    / collection_name
                ),
                directory=objects_dir,
                filename=collection_name,
                autoselect=False,
                instance_collections=False,
                instance_object_data=False,
            )

            self.report(
                {'INFO'},
                f"Added vehicle: {self.vehicle_name}"
            )

            return {'FINISHED'}

        except Exception as ex:

            self.report(
                {'ERROR'},
                str(ex)
            )

            return {'CANCELLED'}