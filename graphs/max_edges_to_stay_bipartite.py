# Maximum number of edges to be added to a tree so that it stays a Bipartite graph

from collections import defaultdict


class Graph():
    def __init__(self, v):
        self.vertices = v
        self.graph = defaultdict(list)

    def addEdge(self, fromVtx, toVtx):
        self.graph[fromVtx].append(toVtx)


def color_graph(graph, v, color, current_color, counts):
    color[v-1] = current_color
    if current_color == 0:
        counts["count1"] += 1
    else:
        counts["count2"] += 1

    for i in graph[v]:
        if color[i-1] == current_color:
            return False
        if color[i-1] == -1:
            res = color_graph(graph, i, color, 1 -
                              current_color, counts)
            if not res:
                return res

    return True


def isBipartite(graph, v):
    color = [-1 for i in range(1, v+1)]
    counts = {
        "count1": 0,
        "count2": 0
    }

    res = False

    for i in range(1, v+1):
        if color[i-1] == -1:
            res = color_graph(graph, i, color, 0, counts)
            if not res:
                return False

    return (color, counts)


g = Graph(5)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(3, 5)

res = isBipartite(g.graph, g.vertices)

if not res:
    print('not bipartite')
else:
    totalEdges = 0
    count1 = res[1]["count1"]
    count2 = res[1]["count2"]
    for i in range(len(g.graph)):
        totalEdges += len(g.graph[i])

    maxEdges = count1 * count2
    remaining = maxEdges - totalEdges
    print(remaining)
