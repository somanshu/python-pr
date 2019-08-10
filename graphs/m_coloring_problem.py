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


def color_graph(graph, v, color, totalVertices, m):
    if v == totalVertices:
        return True

    for i in range(1, m+1):
        if isColorSafe(graph, v, color, i):
            color[v] = i
            res = color_graph(graph, v + 1, color, totalVertices, m)
            if res:
                return res
            color[v] = 0

    return False


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(2, 3)
g.addEdge(3, 0)
g.addEdge(3, 2)
m = 3
color = [0 for i in range(4)]
color_graph(g.graph, 0, color, 4, m)
print(color)
