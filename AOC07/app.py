class BaseNode(object):
    def __init__(self, definition, neighbors):

        self.name = definition.split(' ')[0]
        self.weight = int(definition.split(' ')[1].replace('(', '').replace(')', ''))

        self.neighbor_names = []

        if neighbors is not None:
            self.neighbor_names = neighbors.split(', ')


class Node(object):
    def __init__(self, base_node):
        self.name = base_node.name
        self.self_weight = base_node.weight
        self.neighbors = []

    def add_neighbor(self, n):
        self.neighbors.append(n)


def read_input(path):
    with open(path) as f:
        content = f.read()
        lines = content.split('\n')

        nodes = []

        for line in lines:
            l = line.split(' -> ')

            if len(l) == 1:
                nodes.append(BaseNode(l[0], None))
            else:
                nodes.append(BaseNode(l[0], l[1]))

        return nodes

def get_node_by_name(nodes, name):
    for n in nodes:
        if n.name == name:
            return n

    return None


def construct_graph(base_nodes):
    nodes = []

    for b_node in base_nodes:
        nodes.append(Node(b_node))

    for b_node in base_nodes:
        node = get_node_by_name(nodes, b_node.name)
        for n_name in b_node.neighbor_names:
            n = get_node_by_name(nodes, n_name)
            if n != None:
                node.add_neighbor(n)


if __name__ == "__main__":
    base_nodes_list = read_input('./AOC07/test.io')

    construct_graph(base_nodes_list)

    # a = 'ktlj (57)'
    # b = 'fwft (72) -> ktlj, cntj, xhth'

# rstrip
    # w = a.split(' -> ')
    # z = map(lambda x: x.rstrip(), b.split(' -> '))

