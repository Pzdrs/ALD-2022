import sys


class Graph:
    _nodes: tuple[str] = None
    _matrix = None

    def __init__(self, nodes, adj_matrix) -> None:
        self._nodes = nodes
        self._matrix = adj_matrix

    def get_neighboring_nodes(self, node):
        neighbors = []
        for index, cost in enumerate(self._matrix[self._nodes.index(node)]):
            if cost != 999:
                neighbors.append((self._nodes[index], cost))
        return neighbors


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
