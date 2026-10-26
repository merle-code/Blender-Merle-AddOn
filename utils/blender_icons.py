import bpy.utils.previews # type: ignore

from pathlib import Path

_icons = None


def register_icons():

    global _icons

    _icons = bpy.utils.previews.new()

    icons_dir = (
        Path(__file__).parent.parent
        / "icons"
    )

    for icon_file in icons_dir.glob("*.png"):

        _icons.load(
            icon_file.stem,
            str(icon_file),
            'IMAGE'
        )


def unregister_icons():

    global _icons

    if _icons:
        bpy.utils.previews.remove(_icons)
        _icons = None


def get_icon_id(icon_name):

    global _icons

    if (
        _icons
        and icon_name in _icons
    ):
        return _icons[icon_name].icon_id

    return 0