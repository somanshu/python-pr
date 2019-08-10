# https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/

import math

from collections import defaultdict


class Edge():
    def __init__(self, v1, v2, wt):
        self.v1 = self.v1
        self.v2 = self.v2
        self.wt = wt


class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, fromvtx, tovtx, wt):
        self.graph[fromvtx].append((tovtx, wt))
        self.graph[tovtx].append((fromvtx, wt))

    def getMinKeyVertex(self, mstSet, dist):
        minimum = math.inf
        minVertex = None

        for i in range(self.v):
            if not mstSet[i] and dist[i] != math.inf and dist[i] < minimum:
                minimum = dist[i]
                minVertex = i

        return minVertex

    def prims(self):
        dist = [math.inf for i in range(self.v)]
        mstSet = [False for i in range(self.v)]
        dist[0] = 0
        mstSet[0] = True
        minVertex = 0
        g = Graph(self.v)

        for i in range(self.v):
            for (j, wt) in self.graph[minVertex]:
                if dist[j] > wt:
                    dist[j] = wt

            vertex = self.getMinKeyVertex(mstSet, dist)
            if vertex == None:
                break

            g.addEdge(minVertex, vertex, dist[vertex])
            minVertex = vertex
            mstSet[minVertex] = True

        return g


g = Graph(9)
g.addEdge(0, 1, 4)
g.addEdge(0, 7, 8)
g.addEdge(1, 2, 8)
g.addEdge(1, 7, 11)
g.addEdge(2, 3, 7)
g.addEdge(2, 5, 4)
g.addEdge(2, 8, 2)
g.addEdge(3, 4, 9)
g.addEdge(3, 5, 14)
g.addEdge(4, 5, 10)
g.addEdge(5, 6, 2)
g.addEdge(6, 7, 1)
g.addEdge(6, 8, 6)
g.addEdge(7, 8, 7)
res = g.prims()
print(res)
