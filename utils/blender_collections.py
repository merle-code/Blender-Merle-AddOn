import bpy


def create_collection(collection_name):

    collection = bpy.data.collections.get(
        collection_name
    )

    if collection:
        return collection

    collection = bpy.data.collections.new(
        collection_name
    )

    bpy.context.scene.collection.children.link(
        collection
    )

    return collection

def move_to_collection(obj, collection):

    for col in obj.users_collection:
        col.objects.unlink(obj)

    collection.objects.link(obj)