# Minimum number of edges between two vertices of a Graph

from collections import defaultdict


class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, fromVtx, toVtx):
        self.graph[fromVtx].append(toVtx)
        self.graph[toVtx].append(fromVtx)


def dfs(v, graph, dest, visited):
    if v == dest:
        return 0

    visited[v] = True
    minEdges = 9999

    for i in graph[v]:
        if not visited[i]:
            edges = 1 + dfs(i, graph, dest, visited)
            if edges < minEdges:
                minEdges = edges

    visited[v] = False
    return minEdges


def bfs(source, dest, graph, visited):
    queue = []
    visited[source] = True
    queue.append((source, 0))

    while len(queue) > 0:
        (vertex, edges) = queue.pop(0)

        for i in graph[vertex]:
            if i == dest:
                return edges + 1

            if not visited[i]:
                visited[i] = True
                queue.append((i, edges + 1))

    return False


g = Graph(9)
g.addEdge(0, 1)
g.addEdge(0, 7)
g.addEdge(1, 7)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(2, 5)
g.addEdge(2, 8)
g.addEdge(3, 4)
g.addEdge(3, 5)
g.addEdge(4, 5)
g.addEdge(5, 6)
g.addEdge(6, 7)
g.addEdge(7, 8)
source = 0
dest = 5
visited = [False for i in range(g.v)]
# minEdges = dfs(source, g.graph, dest, visited)
res = bfs(source, dest, g.graph, visited)
print(res)
