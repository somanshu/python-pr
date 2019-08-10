from collections import defaultdict


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, fromVtx, toVtx):
        self.graph[fromVtx].append(toVtx)


def isColorSafe(graph, v, color, current_color):
    for i in graph[v]:
        if color[i] == current_color:
            return False

    return True


def color_graph(graph, v, color, current_color):
    color[v] = current_color

    for i in graph[v]:
        if color[i] == current_color:
            return False
        if color[i] == -1:
            res = color_graph(graph, i, color, 1 - current_color)
            if not res:
                return res

    return True


def isBipartite(graph, v):
    color = [-1 for i in range(v)]

    res = False

    for i in range(v):
        if color[i] == -1:
            res = color_graph(graph, i, color, 0)
            if not res:
                return False

    return res


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 3)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 1)
g.addEdge(2, 3)
g.addEdge(3, 0)
g.addEdge(3, 2)

print(isBipartite(g.graph, 4))
