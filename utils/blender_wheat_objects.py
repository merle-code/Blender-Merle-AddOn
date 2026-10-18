import bpy

from ..config import wheat

def create_wheat(node_group):

    bpy.ops.curve.primitive_bezier_curve_add()

    obj = bpy.context.active_object

    obj.name = wheat.DEFAULT_BASE_NAME

    modifier = obj.modifiers.new(
        name="GeometryNodes",
        type='NODES'
    )

    modifier.node_group = node_group

    return obj
