# Find if there is a path of more than k length from a source
# https://www.geeksforgeeks.org/find-if-there-is-a-path-of-more-than-k-length-from-a-source/

from collections import defaultdict


class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, fromvtx, tovtx, weight):
        self.graph[fromvtx].append((tovtx, weight))
        self.graph[tovtx].append((fromvtx, weight))

    def hasPathGreaterThanK(self, k, source):
        visited = [False for i in range(self.v)]

        if self.checkPathUtil(source, visited, k):
            return True

        return False

    def checkPathUtil(self, vertex, visited, k):
        if k <= 0:
            return True

        visited[vertex] = True

        for (i, weight) in self.graph[vertex]:
            if not visited[i]:
                if self.checkPathUtil(i, visited, k - weight):
                    return True

        visited[vertex] = False
        return False


g = Graph(9)
g.addEdge(0, 1, 4)
g.addEdge(0, 7, 8)
g.addEdge(1, 2, 8)
g.addEdge(1, 7, 11)
g.addEdge(2, 3, 7)
g.addEdge(2, 8, 2)
g.addEdge(2, 5, 4)
g.addEdge(3, 4, 9)
g.addEdge(3, 5, 14)
g.addEdge(4, 5, 10)
g.addEdge(5, 6, 2)
g.addEdge(6, 7, 1)
g.addEdge(6, 8, 6)
g.addEdge(7, 8, 7)

source = 0
k = 62
res = g.hasPathGreaterThanK(k, source)
print(res)

k = 60
res = g.hasPathGreaterThanK(k, source)
print(res)
