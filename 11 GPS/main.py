import sys


class Graph:
    _nodes: tuple[str] = None
    _matrix = None

    def __init__(self, nodes, adj_matrix) -> None:
        self._nodes = nodes
        self._matrix = adj_matrix

    def __get_node_index(self, node):
        if node not in self._nodes:
            raise ValueError(f'Unknown node "{node}"')
        return self._nodes.index(node)

    def __get_node_connections(self, node):
        return self._matrix[self.__get_node_index(node)]

    def __cost(self, node1, node2) -> int:
        """
        :return: the cost of travel between two nodes
        """
        return self.__get_node_connections(node1)[self.__get_node_index(node2)]

    def get_neighboring_nodes(self, node) -> list[tuple[any, int]]:
        """
        :return: a list of tuples, where each tuple represents a neighboring node => (node, cost)
        """
        neighbors = []
        for index, cost in enumerate(self.__get_node_connections(node)):
            if cost != 999:
                neighbors.append((self._nodes[index], cost))
        return neighbors

    def cost(self, *nodes, check_connections=False):
        """
        Calculates the cost of travel between all the specified nodes
        """
        cost = 0
        for i, node in enumerate(nodes):
            if i + 1 == len(nodes):
                break
            next_node = nodes[i + 1]
            intermediary_cost = self.__cost(node, next_node)
            if intermediary_cost == 999 and check_connections:
                raise RuntimeError(f'Node "{node}" and "{next_node}" are not directly connected')
            cost += intermediary_cost
        return cost


CITIES = ("liberec", "ceska-lipa", "chrastava", "new-york", "turnov", "jablonec-nad-nisou")
TIMES = [
    (999, 999, 12, 24, 22, 20),
    (999, 999, 40, 10, 52, 999),
    (12, 40, 999, 20, 999, 999),
    (24, 10, 20, 999, 15, 30),
    (22, 52, 999, 15, 999, 22),
    (20, 999, 999, 30, 22, 999)
]
DISTANCES = (
    (999, 999, 10, 35, 26, 20),
    (999, 999, 47, 30, 67, 999),
    (10, 47, 999, 14, 999, 999),
    (35, 30, 14, 999, 40, 30),
    (26, 67, 999, 40, 999, 24),
    (20, 999, 999, 30, 24, 999)
)

distance_graph = Graph(CITIES, DISTANCES)
time_graph = Graph(CITIES, TIMES)

print(distance_graph.get_neighboring_nodes('liberec'))
print(distance_graph.cost('liberec', 'turnov', check_connections=True))
