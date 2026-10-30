import bpy # type: ignore

class MCA_PT_diagnostics(bpy.types.Panel):
    bl_label = "Diagnostics"
    bl_idname = "MCA_PT_diagnostics"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Custom"
    bl_options = {'DEFAULT_CLOSED'}


    def addRow(self, layout, text, value):

        row = layout.row()

        row.label(text=text)
        row.label(text=str(value))

    def draw(self, context):
        layout = self.layout

        diag = context.scene.mca_diagnostics

        stats_box = layout.box()
        # statystyki

        col = stats_box.column(align=True)

        self.addRow(col, "Materials", str(diag.material_count))
        self.addRow(col, "Images", str(diag.image_count))
        self.addRow(col, "Objects", str(diag.object_count))
        self.addRow(col, "Vertices", str(diag.vertex_count))
        self.addRow(col, "Collections", str(diag.collection_count))
        self.addRow(col, "Node Groups", str(diag.node_group_count))


        options_box = layout.box()
        options_box.prop(
            diag,
            "generate_report"
        )

        options_box.operator(
            "mca.diagnostics_scan",
            icon='VIEWZOOM'
        )