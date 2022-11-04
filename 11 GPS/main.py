import math
import sys
from queue import PriorityQueue


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

    def __get_initial_unvisited(self):
        nodes = list(self._nodes)
        return nodes

    def __backtrace(self, start, end, data):
        """
        Uses the mapped out tree from the Dijkstra pathfinding algorithm and backtraces the full path
        :param start: start node
        :param end: end node
        :param data: mapped tree
        :return: ((full path), cost)
        """
        full_path = [end]
        # convert to a dictionary => {kam se chci dostat:(pres jaky node, cost)}
        paths_dict = {}
        for path in data:
            try:
                paths_dict[path[1]] = (path[0], path[2])
            except IndexError:
                paths_dict[path[1]] = path[0]
        final = paths_dict[end]
        path_segment = final
        while True:
            full_path.append(path_segment[1])
            path_segment = paths_dict[path_segment[1]]

            if path_segment[1] == start:
                full_path.append(path_segment[1])
                break
        # reverse the path because we backtrace from the end, and we want the path starting from the beginning node
        full_path.reverse()
        return tuple(full_path), final[0]

    def _get_neighboring_nodes(self, node, exclude=None) -> list[tuple[any, int]]:
        """
        :return: a list of tuples, where each tuple represents a neighboring node => (node, cost)
        """
        neighbors = []
        for index, cost in enumerate(self.__get_node_connections(node)):
            if cost != 999:
                node = self._nodes[index]
                if exclude and node in exclude:
                    continue
                neighbors.append((node, cost))
        return neighbors

    def dijkstra(self, start, end, backtrace=False, debug=False):
        unvisited_nodes = self.__get_initial_unvisited()
        queue = PriorityQueue()
        # prefill the queue, starting node with cost 0, others with infinity
        for node in self._nodes:
            queue.put((0 if node == start else math.inf, (node,)))

        # initial state
        if debug:
            print("------")
            print(unvisited_nodes)
            print(queue.queue)
            print("------", end='\n\n')

        # this list holds all the mapped nodes
        path_map = []
        while unvisited_nodes:
            current_node = queue.get()
            path_map.append((current_node[0], *current_node[1]))
            if debug:
                print('current node: ' + current_node[1][0], ' | ', str(current_node))
                print('current queue: ' + str(queue.queue))
            neighbors = self._get_neighboring_nodes(
                current_node[1][0],
                exclude=list(set(self._nodes) - set(unvisited_nodes))
            )
            if debug:
                print("neighbors: " + str(neighbors))
            for neighbor in neighbors:
                if debug:
                    print('neighbor: ' + neighbor[0])
                new_queue = PriorityQueue()
                for queue_node in queue.queue:
                    if queue_node[1][0] == neighbor[0]:
                        # od zacatku k neighbor
                        proposed_new_cost = current_node[0] + neighbor[1]
                        if debug:
                            print('current cost to ' + neighbor[0], queue_node[0])
                            print('cost from me to ' + neighbor[0], neighbor[1])
                            print('cost from beginning to me', current_node[0])
                            print('proposed cost from beginning to ' + neighbor[0], current_node[0] + neighbor[1])
                            print('is it worth to change route? ', current_node[0] + neighbor[1] < queue_node[0])
                        if proposed_new_cost < queue_node[0]:
                            new_queue.put((proposed_new_cost, (queue_node[1][0], current_node[1][0])))
                        else:
                            new_queue.put(queue_node)
                    else:
                        new_queue.put(queue_node)
                queue = new_queue
            if debug:
                print('NEW QUEUE: ' + str(queue.queue), end='\n\n\n')
            # this node is fully mapped, mark it as visited
            unvisited_nodes.remove(current_node[1][0])
        return self.__backtrace(start, end, path_map) if backtrace else path_map

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

for line in sys.stdin:
    line = line.strip()
    # [0] - from | [1] - to | [2] - mode
    data = line.split(' ')
    if data[2] == 'nejlepsi':
        result = distance_graph.dijkstra(data[0], data[1], backtrace=True)
        print(f'({time_graph.cost(*result[0])} min, {result[1]} km)', ' -> '.join(result[0]))
    elif data[2] == 'nejkratsi':
        result = time_graph.dijkstra(data[0], data[1], backtrace=True)
        print(f'({result[1]} min, {distance_graph.cost(*result[0])} km)', ' -> '.join(result[0]))
    else:
        raise ValueError('Invalid operation mode.')
