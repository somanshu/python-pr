# https://www.geeksforgeeks.org/find-longest-path-directed-acyclic-graph/

from collections import defaultdict


class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, fromvtx, tovtx, length):
        self.graph[fromvtx].append((tovtx, length))

    def topological_sort(self):
        visited = [False for i in range(self.v)]
        stack = []
        for i in range(self.v):
            if not visited[i]:
                self.topo_util(i, visited, stack)

        stack.reverse()
        return stack

    def topo_util(self, vertex, visited, stack):
        visited[vertex] = True

        for (i, length) in self.graph[vertex]:
            if not visited[i]:
                self.topo_util(i, visited, stack)

        stack.append(vertex)

    def getMaxDist(self):
        stack = self.topological_sort()
        visited = [False for i in range(self.v)]
        dist = [-999 for i in range(self.v)]
        dist[1] = 0

        for i in range(len(stack)):
            for (j, length) in self.graph[stack[i]]:
                if dist[i] == -999:
                    continue
                if dist[j] < dist[i] + length:
                    dist[j] = dist[i] + length

        print(dist)


g = Graph(6)
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 3)
g.addEdge(1, 3, 6)
g.addEdge(1, 2, 2)
g.addEdge(2, 4, 4)
g.addEdge(2, 5, 2)
g.addEdge(2, 3, 7)
g.addEdge(3, 5, 1)
g.addEdge(3, 4, -1)
g.addEdge(4, 5, -2)
g.getMaxDist()
