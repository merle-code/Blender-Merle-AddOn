import bpy # type: ignore

class MCA_PT_diagnostics(bpy.types.Panel):
    bl_label = "Diagnostics"
    bl_idname = "MCA_PT_diagnostics"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Custom"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        box.label(text="Diagnostics")

        diag = context.scene.mca_diagnostics

        box.label(
            text=f"Materials: {diag.material_count}"
        )

        box.label(
            text=f"Images: {diag.image_count}"
        )

        box.label(
            text=f"Objects: {diag.object_count}"
        )

        box.label(
            text=f"Vertices: {diag.vertex_count}"
        )

        diag = context.scene.mca_diagnostics

        box.prop(
            diag,
            "generate_report"
        )

        box.operator(
            "mca.diagnostics_scan",
            icon='VIEWZOOM'
        )