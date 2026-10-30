import bpy # type: ignore

class DiagnosticsProperties(bpy.types.PropertyGroup):

    generate_report: bpy.props.BoolProperty(
        name="Generate Report",
        default=False
    ) # type: ignore

    material_count: bpy.props.IntProperty(
        name="Materials",
        default=0
    ) # type: ignore

    image_count: bpy.props.IntProperty(
        name="Images",
        default=0
    ) # type: ignore

    object_count: bpy.props.IntProperty(
        name="Objects",
        default=0
    ) # type: ignore

    vertex_count: bpy.props.IntProperty(
        name="Vertices",
        default=0
    ) # type: ignore

    collection_count: bpy.props.IntProperty(
        name="Collections",
        default=0
    ) # type: ignore

    node_group_count: bpy.props.IntProperty(
        name="Node Groups",
        default=0
    ) # type: ignore