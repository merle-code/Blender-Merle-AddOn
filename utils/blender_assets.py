import bpy # type: ignore
from pathlib import Path

from ..config import wheat # type: ignore


def get_assets_dir():
    return Path(__file__).parent.parent / "assets"


def get_wheat_blend_file():
    return get_assets_dir() / wheat.BLEND_FILE_NAME


   
def get_wheat_node_group():
    import logging

    logger = logging.getLogger(__name__)



    ng = bpy.data.node_groups.get(wheat.NODE_GROUP_NAME)

    if ng is None:
        blend_file = get_wheat_blend_file()
        
        if not blend_file.exists():
            logger.error(
                f"Asset file not found: {blend_file}"
            )
            logger.error(
                f"Node Group: '{wheat.NODE_GROUP_NAME}' not loaded"
            )
            return None
        ng = append_wheat_node_group(blend_file)
    
    return ng


def append_wheat_node_group(blend_file):

    if bpy.data.node_groups.get(
        wheat.NODE_GROUP_NAME
    ):
        return bpy.data.node_groups[
            wheat.NODE_GROUP_NAME
        ]

    directory = (
        str(blend_file)
        + "/NodeTree/"
    )

    bpy.ops.wm.append(
        directory=directory,
        filename=wheat.NODE_GROUP_NAME
    )

    return bpy.data.node_groups.get(
        wheat.NODE_GROUP_NAME
    )