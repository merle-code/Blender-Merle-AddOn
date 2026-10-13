
def set_gn_input(obj, input_name, value):

    mod = obj.modifiers['GeometryNodes']

    socket = mod.node_group.interface.items_tree[input_name]

    mod.properties.inputs[socket.identifier]['value'] = value


def get_gn_input(obj, input_name):

    mod = obj.modifiers['GeometryNodes']

    socket = mod.node_group.interface.items_tree[input_name]

    return mod.properties.inputs[
        socket.identifier
    ]['value']

