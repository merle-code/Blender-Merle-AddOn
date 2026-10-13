import bpy # type: ignore
import random

from ..config import wheat

class WheatProperties(bpy.types.PropertyGroup):

    base_name: bpy.props.StringProperty(
        name="Base Name",
        default=wheat.DEFAULT_BASE_NAME,
        maxlen=64
    ) # type: ignore

    count: bpy.props.IntProperty(
        name="Count",
        default=wheat.DEFAULT_COUNT,
        min=1,
        max=1000
    ) # type: ignore

    collection_name: bpy.props.StringProperty(
        name="Collection",
        default=wheat.DEFAULT_COLLECTION_NAME,
        maxlen=64
    ) # type: ignore

    seed_start: bpy.props.IntProperty(
        name="Seed Start",
        default=wheat.DEFAULT_START_SEED,
        min=0
    ) # type: ignore

    seed: bpy.props.IntProperty(
        name="Seed",
        default=random.randrange(0, 9999),
        min=0
    ) # type: ignore

    convert_to_mesh: bpy.props.BoolProperty(
        name="Convert to Mesh",
        default=False
    ) # type: ignore

    density: bpy.props.FloatProperty(
        name="Density",
        default=wheat.DEFAULT_DENSITY,
        min=0.01,
    ) # type: ignore

    jitter: bpy.props.BoolProperty(
        name="Jitter",
        default=False
    ) # type: ignore