# Roots of a tree which give minimum height
# https://www.geeksforgeeks.org/roots-tree-gives-minimum-height/

from collections import defaultdict


class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, fromvtx, tovtx):
        self.graph[fromvtx].append(tovtx)
        self.graph[tovtx].append(fromvtx)

    def getFurthestVtxWithDistance(self, vertex):
        visited = [False for i in range(self.v)]
        queue = []
        queue.append((vertex, 0))
        visited[vertex] = True

        maxDistance = 0
        farthestVtx = vertex

        while len(queue) > 0:
            (v, d) = queue.pop(0)

            if d > maxDistance:
                maxDistance = d
                farthestVtx = v

            for i in self.graph[v]:
                if not visited[i]:
                    visited[i] = True
                    queue.append((i, d+1))

        return (farthestVtx, maxDistance)

    def getDiameter(self):
        (v1, d1) = self.getFurthestVtxWithDistance(0)
        (v2, d2) = self.getFurthestVtxWithDistance(v1)
        return (v1, v2, d2)

    def getRootsWithMinHeight(self):
        (v1, v2, d) = self.getDiameter()
        visited1 = [False for i in range(self.v)]
        visited2 = [False for i in range(self.v)]
        queue1 = []
        queue2 = []
        queue1.append(v1)
        queue2.append(v2)
        visited1[v1] = True
        visited2[v2] = True
        rootsCount = 2

        if d % 2 == 0:
            rootsCount = 1

        while len(queue1) > 0 and len(queue2) > 0:
            v1 = queue1.pop(0)
            v2 = queue2.pop(0)

            for i in self.graph[v1]:
                if visited2[i] == True:
                    return (v1, v2) if rootsCount > 1 else i
                if not visited1[i] and not visited2[i]:
                    visited1[i] = True
                    queue1.append(i)

            for i in self.graph[v2]:
                if visited1[i] == True:
                    return (v1, v2) if rootsCount > 1 else i
                if not visited2[i] and not visited1[i]:
                    visited2[i] = True
                    queue2.append(i)


g = Graph(7)
g.addEdge(0, 3)
g.addEdge(1, 3)
g.addEdge(2, 3)
g.addEdge(4, 3)
g.addEdge(5, 4)
g.addEdge(5, 6)
res = g.getRootsWithMinHeight()
print(res)
