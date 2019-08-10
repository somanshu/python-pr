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

    def getFurthestVertex(self, vertex, parent):
        visited = [False for i in range(self.v + 1)]

        if parent != None:
            visited[parent] = True

        queue = []
        visited[vertex] = True
        queue.append((vertex, 0))
        maxDistance = 0
        farthestVertex = vertex

        while len(queue) > 0:
            (v, d) = queue.pop(0)
            if d > maxDistance:
                maxDistance = d
                farthestVertex = v
            for i in self.graph[v]:
                if not visited[i]:
                    visited[i] = True
                    queue.append((i, d+1))

        return (farthestVertex, maxDistance)

    def getPath(self, vertex, parent):
        (v1, d1) = self.getFurthestVertex(vertex, parent)
        if v1 == vertex:
            return 0
        (v2, d2) = self.getFurthestVertex(v1, parent)
        return d2

    def maximizePaths(self, vertex, parent, maxProduct):
        for i in self.graph[vertex]:
            if i != parent:
                p1 = self.getPath(i, vertex)
                p2 = self.getPath(vertex, i) if p1 != 0 else 0
                product = p1 * p2

                if product > maxProduct[0]:
                    maxProduct[0] = product

                self.maximizePaths(i, vertex, maxProduct)

    def maxProductPaths(self):
        maxProduct = [1]
        self.maximizePaths(1, None, maxProduct)
        return maxProduct[0]


g = Graph(8)
g.addEdge(1, 8)
g.addEdge(2, 6)
g.addEdge(3, 1)
g.addEdge(5, 3)
g.addEdge(7, 8)
g.addEdge(8, 4)
g.addEdge(8, 6)
res = g.maxProductPaths()
print(res)
