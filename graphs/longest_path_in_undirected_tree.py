# Longest path in an undirected tree
# https://www.geeksforgeeks.org/longest-path-undirected-tree/

from collections import defaultdict


class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, fromvtx, tovtx):
        self.graph[fromvtx].append(tovtx)
        self.graph[tovtx].append(fromvtx)

    def bfs(self, vertex):
        visited = [False for i in range(self.v)]
        queue = []
        queue.append((vertex, 0))
        visited[vertex] = True
        maxDistance = 0
        farthestVertex = vertex

        while len(queue) > 0:
            (v, distance) = queue.pop(0)
            if distance > maxDistance:
                maxDistance = distance
                farthestVertex = v

            for i in self.graph[v]:
                if not visited[i]:
                    visited[i] = True
                    queue.append((i, distance + 1))

        return (farthestVertex, maxDistance)

    def getLongestPath(self):
        (fvtx, fdist) = self.bfs(0)
        (svtx, sdist) = self.bfs(fvtx)
        print(fvtx, svtx)
        return sdist


g = Graph(10)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(2, 9)
g.addEdge(2, 4)
g.addEdge(4, 5)
g.addEdge(1, 6)
g.addEdge(6, 7)
g.addEdge(6, 8)
res = g.getLongestPath()
print(res)
