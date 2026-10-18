import bpy

from ..config import thunders

def create_thunderball(node_group):

    bpy.ops.curve.primitive_bezier_curve_add()

    obj = bpy.context.active_object

    obj.name = thunders.THUNDERBALL_DEFAULT_BALL_NAME

    modifier = obj.modifiers.new(
        name="GeometryNodes",
        type='NODES'
    )

    modifier.node_group = node_group

    return obj
