# Topological sorting
# https://www.geeksforgeeks.org/topological-sorting/

from collections import defaultdict


class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, fromvtx, tovtx):
        self.graph[fromvtx].append(tovtx)

    def dfs(self, vertex, visited, stack):
        visited[vertex] = True

        for i in self.graph[vertex]:
            if not visited[i]:
                self.dfs(i, visited, stack)

        stack.append(vertex)

    def topological_sort(self):
        visited = [False for i in range(self.v)]
        stack = []

        for i in range(self.v):
            if not visited[i]:
                self.dfs(i, visited, stack)

        stack.reverse()
        print(stack)


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.topological_sort()
