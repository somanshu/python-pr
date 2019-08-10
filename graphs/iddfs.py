# https://www.geeksforgeeks.org/iterative-deepening-searchids-iterative-deepening-depth-first-searchiddfs/


from collections import defaultdict


class Graph():
    def __init__(self, v, maxDepth, source, destination):
        self.v = v
        self.graph = defaultdict(list)
        self.maxDepth = maxDepth
        self.source = source
        self.destination = destination

    def addEdge(self, fromvtx, tovtx):
        self.graph[fromvtx].append(tovtx)
        self.graph[tovtx].append(fromvtx)

    def iddfs(self):
        for i in range(self.maxDepth):
            if self.dls(i, self.source):
                return True

        return False

    def dls(self, maxDepth, vertex):
        if vertex == self.destination:
            return True

        if maxDepth <= 0:
            return False

        for i in self.graph[vertex]:
            if self.dls(maxDepth - 1, i):
                return True

        return False


g = Graph(7, 3, 0, 6)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(2, 6)

res = g.iddfs()
print(res)
