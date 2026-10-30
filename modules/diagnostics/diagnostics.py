import bpy # type: ignore
import os

def get_material_count():
    return len(bpy.data.materials)

def get_image_count():
    return len(bpy.data.images)

def get_vertex_count():
    total = 0

    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            total += len(obj.data.vertices)

    return total

def get_object_count():
    return len(bpy.data.objects)

def get_collection_count():
    return len(bpy.data.collections)

def get_node_group_count():
    return len(bpy.data.node_groups)

def get_node_groups():

    groups = []

    for group in sorted(
        bpy.data.node_groups,
        key=lambda g: g.name.lower()
    ):

        groups.append({
            "name": group.name,
            "users": group.users,
            "type": group.bl_idname,
        })

    return groups

def get_collection_parent(collection):

    for parent in bpy.data.collections:

        if collection.name in parent.children.keys():
            return parent.name
        
def get_collections():

    collections = []

    for collection in sorted(
        bpy.data.collections,
        key=lambda c: c.name.lower()
    ):

        collections.append({
            "name": collection.name,
            "parent": get_collection_parent(collection),
            "objects": len(collection.objects),
        })

    return collections

def append_collection_tree(
    report,
    tree,
    collections_map,
    node,
    prefix="",
    is_last=True
):

    connector = ""

    if prefix:
        connector = "└── " if is_last else "├── "

    objects = collections_map[node]["objects"]

    report.append(
        f"{prefix}{connector}'{node}' ({objects})"
    )

    children = sorted(tree[node])

    next_prefix = prefix + (
        "    " if is_last else "│   "
    )

    for i, child in enumerate(children):
        append_collection_tree(
            report,
            tree,
            collections_map,
            child,
            next_prefix,
            i == len(children) - 1
        )

def build_collection_tree(collections):

    tree = {}

    for col in collections:
        tree[col["name"]] = []

    for col in collections:

        parent = col["parent"]

        if parent:
            tree[parent].append(col['name'])

    return tree

def get_material_type(mat):

    if not mat.use_nodes:
        return "NO_NODES"

    has_image = False
    has_procedural = False

    procedural_nodes = {
        'NOISE_TEXTURE',
        'VORONOI_TEXTURE',
        'MUSGRAVE_TEXTURE',
        'WAVE_TEXTURE',
        'MAGIC_TEXTURE',
        'BRICK_TEXTURE',
        'CHECKER_TEXTURE',
        'WHITE_NOISE_TEXTURE',
    }

    for node in mat.node_tree.nodes:

        if node.type == 'TEX_IMAGE':
            has_image = True

        if node.type in procedural_nodes:
            has_procedural = True

    if has_image and has_procedural:
        return "MIXED"

    if has_image:
        return "IMAGE_TEXTURE"

    return "PROCEDURAL"

def get_materials():

    materials = []

    for mat in sorted(
        bpy.data.materials,
        key=lambda m: m.name.lower()
    ):

        materials.append({
            "name": mat.name,
            "users": mat.users,
            "type": get_material_type(mat),
        })

    return materials

def get_image_size(image):
    if image.packed_file:
        return len(image.packed_file.data)
    else:
        try:
            return os.path.getsize(
                bpy.path.abspath(image.filepath)
            )
        except OSError:
            return 0

def get_image_type(img):

    if img.name == "Render Result":
        return "RENDER_RESULT"

    if img.name == "Viewer Node":
        return "VIEWER_NODE"

    if img.source == 'GENERATED':
        return "GENERATED"

    return "IMAGE"

def get_images():
    images = []
    for img in sorted(
        bpy.data.images,
        key=lambda img: get_image_size(img),
        reverse=True
    ):
        
        images.append({
            "name": img.name,
            "type": get_image_type(img),
            "users": img.users,
            "packed": True if img.packed_file else False,
            "resolution": f"{img.size[0]}x{img.size[1]}",
            "size": get_image_size(img),
            "path": img.filepath,
            "missing": not os.path.exists(
                bpy.path.abspath(img.filepath)
            ) if img.filepath else False,
        })
    
    return images

def get_object_points(obj):

    if obj.type == 'MESH':
        return len(obj.data.vertices)

    elif obj.type == 'CURVE':
        return sum(
            len(spline.bezier_points)
            + len(spline.points)
            for spline in obj.data.splines
        )

    elif obj.type == 'SURFACE':
        return sum(
            len(spline.points)
            for spline in obj.data.splines
        )

    elif obj.type == 'FONT':
        return len(obj.data.body)

    elif obj.type == 'META':
        return len(obj.data.elements)

    return 0

def get_objects():

    objects = []

    for obj in sorted(
        bpy.data.objects,
        key=lambda o: get_object_points(o),
        reverse=True
    ):

        materials = (
            len(obj.material_slots)
            if hasattr(obj, "material_slots")
            else 0
        )

        objects.append({
            "name": obj.name,
            "type": obj.type,
            "points": get_object_points(obj),
            "materials": materials,
        })

    return objects


def collect_diagnostics():

    materials = get_materials()
    images = get_images()
    objects = get_objects()
    collections = get_collections()
    node_groups = get_node_groups()

    return {
        "materials_count": len(materials),
        "materials": materials,
        "images_count": len(images),
        "images": images,
        "vertices_count": get_vertex_count(),
        "objects_count": len(objects),
        "objects": objects,
        "collections_count": len(collections),
        "collections": collections,
        "node_groups_count": len(node_groups),
        "node_groups": node_groups,
    }


def generate_report(stats):

    report = []

    report.append("=== MCA DIAGNOSTICS ===")
    report.append("")

    report.append("GENERAL")
    report.append("----------------------------------------")
    report.append(f"Materials   : {stats['materials_count']}")
    report.append(f"Images      : {stats['images_count']}")
    report.append(f"Objects     : {stats['objects_count']}")
    report.append(f"Vertices    : {stats['vertices_count']}")
    report.append(f"Collections : {stats['collections_count']}")
    report.append(f"Node Groups : {stats['node_groups_count']}")
    report.append("")
    report.append("")

    report.append("MATERIALS")
    report.append("----------------------------------------")
    report.append(
        f"{'#':>3} "
        f"{'Name':<30} "
        f"{'Users':<6} "
        f"Type"
    )
    report.append(
        f"{'-'*3} "
        f"{'-'*30} "
        f"{'-'*6} "
        f"{'-'*12}"
    )

    for num, mat in enumerate(stats["materials"], start=1):
        report.append(
            f"{num:>3} "
            f"{mat['name']:<30.30} "
            f"{mat['users']:<6} "
            f"{mat['type']}"
        )

    report.append("")
    report.append("IMAGES")
    report.append("--------------------------------------------------------------------------------")
    report.append(
        f"{'#':>3} "
        f"{'Name':<30} "
        f"{'Type':<15} "
        f"{'Users':<5} "
        f"{'Packed':<6} "
        f"{'Resolution':<10} "
        f"{'Size':>8}"
    )

    report.append(
        f"{'-'*3} "
        f"{'-'*30} "
        f"{'-'*15} "
        f"{'-'*5} "
        f"{'-'*6} "
        f"{'-'*10} "
        f"{'-'*8}"
    )

    for num, img in enumerate(stats["images"], start=1):

        packed = "YES" if img["packed"] else "NO"

        report.append(
            f"{num:>3} "
            f"{img['name']:<30.30} "
            f"{img['type']:<15} "
            f"{img['users']:<5} "
            f"{packed:<6} "
            f"{img['resolution']:<10} "
            f"{img['size']/1024:>7.1f}K"
        )

    report.append("")
    report.append("IMAGE PATHS")
    report.append("--------------------------------------------------------------------------------")

    report.append(
        f"{'Type':>15} "
        f"{'Name':<30.30} "
        f"{'Missing':<9} "
        f"{'Path'} "
    )
    report.append(
        f"{'-'*15} "
        f"{'-'*30} "
        f"{'-'*9} "
        f"{'-'*50}"
    )
    for img in stats["images"]:
        
        missing = "MISSING" if img["missing"] else ""
        report.append(
            f"{img['type']:<15} "
            f"{img['name']:<30.30} "
            f"{missing:9} "
            f"{img['path']}"
        )

    report.append("")

    report.append("OBJECTS")
    report.append("--------------------------------------------------------------------------------")

    report.append(
        f"{'#':>3} "
        f"{'Name':<30} "
        f"{'Type':<10} "
        f"{'Points':>10} "
        f"{'Materials':>10}"
    )

    report.append(
        f"{'-'*3} "
        f"{'-'*30} "
        f"{'-'*10} "
        f"{'-'*10} "
        f"{'-'*10}"
    )

    for num, obj in enumerate(stats["objects"], start=1):

        report.append(
            f"{num:>3} "
            f"{obj['name']:<30.30} "
            f"{obj['type']:<10} "
            f"{obj['points']:>10} "
            f"{obj['materials']:>10}"
        )

    report.append("")
    report.append("COLLECTION TREE")
    report.append("--------------------------------------------------------------------------------")

    tree = build_collection_tree(
        stats["collections"]
    )

    collections_map = {
        c["name"]: c
        for c in stats["collections"]
    }

    roots = [
        c["name"]
        for c in stats["collections"]
        if c["parent"] is None
    ]

    report.append("\\")

    for i, root in enumerate(sorted(roots)):

        last = (i == len(roots) - 1)

        connector = "└── " if last else "├── "

        objects = collections_map[root]["objects"]

        report.append(
            f"{connector}'{root}' ({objects})"
        )

        children = sorted(tree[root])

        for j, child in enumerate(children):

            append_collection_tree(
                report,
                tree,
                collections_map,
                child,
                "    " if last else "│   ",
                j == len(children) - 1
            )

    report.append("")

    report.append("NODE GROUPS")
    report.append("--------------------------------------------------------------------------------")

    report.append(
        f"{'#':>3} "
        f"{'Name':<40} "
        f"{'Users':>6} "
        f"{'Type'}"
    )

    report.append(
        f"{'-'*3} "
        f"{'-'*40} "
        f"{'-'*6} "
        f"{'-'*20}"
    )

    for num, group in enumerate(
        stats["node_groups"],
        start=1
    ):
        report.append(
            f"{num:>3} "
            f"{group['name']:<40.40} "
            f"{group['users']:>6} "
            f"{group['type']}"
        )

    return "\n".join(report)
