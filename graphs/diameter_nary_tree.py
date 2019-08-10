# Diameter of an N-ary tree

from collections import defaultdict


class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, fromvtx, tovtx):
        self.graph[fromvtx].append(tovtx)
        self.graph[tovtx].append(fromvtx)

    def getDiameter(self, vertex, parent):
        diameter = 0
        height = []

        for v in self.graph[vertex]:
            if v != parent:
                (d, h) = self.getDiameter(v, vertex)
                height.append(h+1)
                if d > diameter:
                    diameter = d

        maxHeight = 0
        secondMaxHeight = 0

        for h in height:
            if h > maxHeight:
                secondMaxHeight = maxHeight
                maxHeight = h
            elif h > secondMaxHeight:
                secondMaxHeight = h

        return (max(diameter, maxHeight + secondMaxHeight + 1), max(height) if len(height) > 0 else 0)


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
res = g.getDiameter(0, None)
print(res)
