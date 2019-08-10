# Maximum product of two non-intersecting paths in a tree
# https://www.geeksforgeeks.org/maximum-product-of-two-non-intersecting-paths-in-a-tree/

from collections import defaultdict


class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, fromvtx, tovtx):
        self.graph[fromvtx].append(tovtx)
        self.graph[tovtx].append(fromvtx)

    def dfs(self, vertex, visited, path, allPaths):
        visited[vertex] = True
        path.append(vertex)

        if len(self.graph[vertex]) == 0:
            allPaths.append(path)

        for i in self.graph[vertex]:
            if not visited[i]:
                self.dfs(i, visited, path, allPaths)

        path.pop(-1)
        visited[vertex] = False


g = Graph(8)
g.addEdge(1, 8)
g.addEdge(2, 6)
g.addEdge(3, 1)
g.addEdge(5, 3)
g.addEdge(7, 8)
g.addEdge(8, 4)
g.addEdge(8, 6)

visited = {}

for i in range(1, g.v + 1):
    visited[i] = False

allPaths = []
path = []

v = None
for i, iList in g.graph.items():
    if len(iList) == 1:
        v = i
        break

g.dfs(v, visited, path, allPaths)
print(allPaths)
