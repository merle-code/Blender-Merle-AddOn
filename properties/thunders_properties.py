import bpy # type: ignore

from ..config import thunders

class ThundersProperties(bpy.types.PropertyGroup):

    base_name: bpy.props.StringProperty(
        name="Base Name",
        default=thunders.THUNDERBALL_DEFAULT_BALL_NAME,
        maxlen=64
    ) # type: ignore

    convert_to_mesh: bpy.props.BoolProperty(
        name="Convert to Mesh",
        default=False
    ) # type: ignore

    seed: bpy.props.IntProperty(
        name="Seed",
        default=thunders.DEFAULT_SEED,
        min=0
    ) # type: ignore
