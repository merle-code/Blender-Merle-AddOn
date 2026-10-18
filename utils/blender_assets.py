import bpy # type: ignore
from pathlib import Path
import logging


def get_assets_dir():
    return Path(__file__).parent.parent / "assets"


def get_blend_file(blend_file):
    return get_assets_dir() / blend_file


def append_node_group(
            blend_file,
            node_group_name
        ):

    ng = bpy.data.node_groups.get(
        node_group_name
    )

    if ng:
        return ng

    directory = (
        str(blend_file)
        + "/NodeTree/"
    )

    bpy.ops.wm.append(
        directory=directory,
        filename=node_group_name
    )

    return bpy.data.node_groups.get(
        node_group_name
    )


def get_then_append_node_group(
            blend_file,
            node_group_name
        ):
    logger = logging.getLogger(__name__)

    ng = bpy.data.node_groups.get(
        node_group_name
    )

    if ng:
        return ng

    if not blend_file.exists():
        logger.error(
            f"Asset file not found: {blend_file}"
        )
        logger.error(
            f"Node Group '{node_group_name}' not loaded"
        )
        return None

    return append_node_group(
        blend_file,
        node_group_name
    )