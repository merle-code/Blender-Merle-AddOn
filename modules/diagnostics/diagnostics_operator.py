import bpy # type: ignore

from .diagnostics import (
    get_material_count,
    get_image_count,
    get_vertex_count,
    get_object_count,
    collect_diagnostics,
    generate_report,
)


class MCA_OT_diagnostics_scan(bpy.types.Operator):
    bl_idname = "mca.diagnostics_scan"
    bl_label = "Scan Asset"

    def execute(self, context):

        diag = context.scene.mca_diagnostics

        print("\n=== MCA DIAGNOSTICS ===")

        diag.material_count = get_material_count()
        diag.image_count = get_image_count()
        diag.vertex_count = get_vertex_count()
        diag.object_count = get_object_count()

        stats = collect_diagnostics()

        if diag.generate_report:

            report = generate_report(stats)

            text_name = "MCA_DIAGNOSTICS_REPORT"

            text = bpy.data.texts.get(text_name)

            if not text:
                text = bpy.data.texts.new(text_name)

            text.clear()
            text.write(report)
            self.report(
                {'INFO'},
                f"REPORT GENERATED: {text_name}"
            )
            return {'FINISHED'}

        print(f"Materials: {diag.material_count}")
        print(f"Images:    {diag.image_count}")
        print(f"Vertices:  {diag.object_count}")
        print(f"Vertices:  {diag.vertex_count}")

        self.report(
            {'INFO'},
            f"Materials: {diag.material_count} | "
            f"Images: {diag.image_count} | "
            f"Objects: {diag.object_count}| "
            f"Vertices: {diag.vertex_count}"
        )

        return {'FINISHED'}
