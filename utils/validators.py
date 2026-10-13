import bpy # type: ignore

INVALID_CHARACTERS = ["/", "\\", ":", "*", "?", "\"", "<", ">", "|"]

def validate_wheat_properties(props):

    if not props.base_name.strip():
        return "Base Name cannot be empty"

    if not props.collection_name.strip():
        return "Collection Name cannot be empty"
    
    if props.count < 1:
        return "Count must be greater than 0"

    for char in INVALID_CHARACTERS:
        if char in props.collection_name:
            return f"Collection contains invalid character: {char}"

    collection = bpy.data.collections.get(
        props.collection_name
    )

    if collection and len(collection.objects) > 0:
        return (
            f"Collection '{props.collection_name}' "
            "already exists and is not empty"
        )
    
    return None