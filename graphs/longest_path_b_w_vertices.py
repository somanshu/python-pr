# Longest path between any pair of vertices
# https://www.geeksforgeeks.org/longest-path-between-any-pair-of-vertices/

from collections import defaultdict


class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, fromvtx, tovtx, length):
        self.graph[fromvtx].append((tovtx, length))
        self.graph[tovtx].append((fromvtx, length))

    def dfs(self, vertex, visited):
        visited[vertex] = True
        maxDist = 0

        for (i, length) in self.graph[vertex]:
            if not visited[i]:
                dist = length + self.dfs(i, visited)
                if dist > maxDist:
                    maxDist = dist

        visited[vertex] = False

        return maxDist

    def getMaxDist(self):
        visited = [False for i in range(self.v + 1)]
        maxDist = 0

        for i in range(1, self.v + 1):
            dist = self.dfs(i, visited)
            if dist > maxDist:
                maxDist = dist

        print(maxDist)


g = Graph(6)
g.addEdge(1, 2, 3)
g.addEdge(2, 3, 4)
g.addEdge(2, 6, 2)
g.addEdge(4, 6, 6)
g.addEdge(5, 6, 5)
g.getMaxDist()
