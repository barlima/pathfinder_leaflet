# Helper for trips controller to count the shortest path
from collections import defaultdict
from tsp_solver.greedy import solve_tsp
import math
import json


class Graph:
    def __init__(self):
        self.nodes_amount = 0
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.nodes_amount += 1

    def add_edges(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance


class Link:

    def __init__(self, A, B, distance):
        self.source = A
        self.sink = B
        self.weight = distance


class Node:

    def __init__(self, name):
        self.name = name


def prepare_shortest_path(points, routes_text):
    links = translate_text_to_routes(routes_text)
    points = json.loads(points)

    map_graph = Graph()

    for link in links:
        # if graph if complete adding sources only should provide all of the nodes
        map_graph.add_node(link.source)
        map_graph.add_node(link.sink)
        map_graph.add_edges(link.source, link.sink, link.weight)

    # If source == sink use Travelling Salesman Problem
    if '0' == '1':
        distance, path = tsp(map_graph)
    else:
        distance, path = shortest_hamiltonian(map_graph, '0', '1')

    return distance, path


def translate_text_to_routes(routes_text):
    routes_text = routes_text.split(':')
    routes = []

    for route in routes_text:
        data = route.split('/')
        if len(data) >= 3:
            routes.append(Link(data[0], data[1], float(data[2])))

    return routes


def dijsktra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited [edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def hamiltonian(graph, source, sink):
    visited = {source: 0}
    last = source
    path = [source]
    distance = 0

    nodes = set(graph.nodes)
    nodes.remove(source)
    nodes.remove(sink)

    while nodes:
        min_value = math.inf
        for node in nodes:
            try:
                if graph.distances[(last, node)] < min_value:
                    min_value = graph.distances[(last, node)]
                    next_node = node
                    distance += min_value
            except KeyError:
                continue
        last = next_node
        visited[next_node] = min_value
        path.append(next_node)
        nodes.remove(last)

    path.append(sink)

    return path, distance


def shortest_hamiltonian(graph, source, sink):
    path = [source]
    path_swap = []

    distances = [0]
    distances_swap = []

    nodes = list(graph.nodes)
    nodes.remove(source)
    if source != sink:
        nodes.remove(sink)

    for n in nodes:
        for i in range(len(distances)):
            for m in nodes:
                if m not in path[i].split(':'):
                    last = path[i].split(':')[-1]
                    try:
                        distances_swap.append(distances[i] + graph.distances[(last, m)])
                        path_swap.append(path[i] + ':' + m)
                    except KeyError:
                        'KeyError occurred'
                        distances_swap.append(distances[i] + math.inf)
                        path_swap.append(path[i] + ':' + m)
        distances = distances_swap
        distances_swap = []
        path = path_swap
        path_swap = []

    for i in range(len(distances)):
        last = path[i].split(':')[-1]
        try:
            distances_swap.append(distances[i] + graph.distances[(last, sink)])
            path_swap.append(path[i] + ':' + sink)
        except KeyError:
            print('KeyError occurred')
            distances_swap.append(distances[i] + math.inf)
            path_swap.append(path[i] + ':' + sink)
    distances = distances_swap
    path = path_swap

    return min(distances), path[distances.index(min(distances))].split(':')


def tsp(graph):
    matrix = []
    line = []

    for n in graph.nodes:
        for m in graph.nodes:
            if n == m:
                line.append(0)
            else:
                line.append(graph.distances[(n, m)])
        matrix.append(line)
        line = []

    path = solve_tsp(matrix)
    # print(path)
    # path.append(path[0])
    # print(path)
    # ToDo: count the distance in a proper way
    distance = 1000

    return distance, [str(p) for p in path]


def set_proper_order(points, order):
    points_in_order = []
    points = json.loads(points)

    for i in range(len(points)):
        points_in_order.insert(i, points[int(order[i])])

    return points_in_order


def clear_table(table):
    clean_table = []

    for i in table:
        clean_table.append(i[1:-1].split(','))

    return clean_table
