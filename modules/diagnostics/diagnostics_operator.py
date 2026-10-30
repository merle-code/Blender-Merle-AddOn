import bpy # type: ignore

from .diagnostics import (
    get_material_count,
    get_image_count,
    get_vertex_count,
    get_object_count,
    collect_diagnostics,
    generate_report,
    get_collection_count,
    get_node_group_count,
)


class MCA_OT_diagnostics_scan(bpy.types.Operator):
    bl_idname = "mca.diagnostics_scan"
    bl_label = "Scan Asset"

    def execute(self, context):

        diag = context.scene.mca_diagnostics

        self.report(
                        {'INFO'},
                        "START MCA DIAGNOSTIC REPORT"
                    )
        diag.material_count = get_material_count()
        diag.image_count = get_image_count()
        diag.vertex_count = get_vertex_count()
        diag.object_count = get_object_count()
        diag.collection_count = get_collection_count()
        diag.node_group_count = get_node_group_count()

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

        print(f"Materials:  {diag.material_count}")
        print(f"Images:     {diag.image_count}")
        print(f"Vertices:   {diag.object_count}")
        print(f"Vertices:   {diag.vertex_count}")
        print(f"Collections:{diag.collection_count}")
        print(f"Node Groups:{diag.node_group_count}")

        self.report(
            {'INFO'},
            f"Materials: {diag.material_count} | "
            f"Images: {diag.image_count} | "
            f"Objects: {diag.object_count}| "
            f"Vertices: {diag.vertex_count}| "
            f"Collections:{diag.collection_count}| "
            f"Node Groups:{diag.node_group_count}| "
        )

        return {'FINISHED'}
