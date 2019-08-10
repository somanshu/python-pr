# Count all possible paths between two vertices
from collections import defaultdict


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, srcV, desV):
        self.graph[srcV].append(desV)


def count_paths(v, dest, visited, graph):
    visited[v] = True

    if v == dest:
        return 1

    val = 0

    for i in graph[v]:
        if not visited[i]:
            val += count_paths(i, dest, visited, graph)
            visited[i] = False

    return val


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(1, 3)
source = 2
destination = 3

visited = [False for i in range(4)]
res = count_paths(source, destination, visited, g.graph)
print(res)
