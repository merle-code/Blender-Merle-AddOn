from ..config import thunders

from .blender_assets import (
    get_blend_file,
    get_then_append_node_group,
)


def get_thunderball_blend_file():
    return get_blend_file(thunders.BLEND_FILE_NAME)

   
def get_thunderball_node_group():
    return get_then_append_node_group(get_thunderball_blend_file(),
                          thunders.THUNDERBALL_NODE_GROUP_NAME)

