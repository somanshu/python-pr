# Detect cycle in directed graph
# https://www.geeksforgeeks.org/detect-cycle-in-a-graph/

from collections import defaultdict


class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, fromvtx, tovtx):
        self.graph[fromvtx].append(tovtx)

    def dfs(self, visited, recStack, vertex):
        visited[vertex] = True
        recStack[vertex] = True

        for i in self.graph[vertex]:
            if not visited[i]:
                if self.dfs(visited, recStack, i):
                    return True
            elif recStack[i]:
                return True

        recStack[vertex] = False
        return False

    def detectCycle(self):
        visited = [False for i in range(self.v)]
        recStack = [False for i in range(self.v)]

        for i in range(self.v):
            if not visited[i]:
                if self.dfs(visited, recStack, i):
                    return True

        return False


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
res = g.detectCycle()
print(res)
