from ..config import wheat

from .blender_assets import (
    get_blend_file,
    get_then_append_node_group,
)


def get_wheat_blend_file():
    return get_blend_file(wheat.BLEND_FILE_NAME)

   
def get_wheat_node_group():
    return get_then_append_node_group(get_wheat_blend_file(),
                          wheat.NODE_GROUP_NAME)

