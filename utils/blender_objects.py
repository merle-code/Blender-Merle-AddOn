import bpy # type: ignore


def duplicate_object(obj):

    copy = obj.copy()
    if obj.data:
        copy.data = obj.data.copy()

    return copy


def remove_empty_material_slots(obj):

    bpy.ops.object.select_all(action='DESELECT')

    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

    for i in reversed(range(len(obj.material_slots))):

        if obj.material_slots[i].material is None:

            obj.active_material_index = i

            bpy.ops.object.material_slot_remove()


def convert_to_mesh(obj):

    bpy.ops.object.select_all(action='DESELECT')

    obj.select_set(True)

    bpy.context.view_layer.objects.active = obj

    bpy.ops.object.convert(
        target='MESH'
    )


def delete_object(obj):

    bpy.data.objects.remove(
        obj,
        do_unlink=True
    )