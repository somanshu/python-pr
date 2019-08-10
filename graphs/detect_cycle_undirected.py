# Detect cycle in undirected graph
# https://www.geeksforgeeks.org/detect-cycle-undirected-graph/

from collections import defaultdict


class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, fromvtx, tovtx):
        self.graph[fromvtx].append(tovtx)
        self.graph[tovtx].append(fromvtx)

    def dfs(self, vertex, parent, visited):
        visited[vertex] = True

        for i in self.graph[vertex]:
            if not visited[i]:
                if self.dfs(i, vertex, visited):
                    return True

            elif i != parent:
                return True

        return False

    def detectCycle(self):
        visited = [False for i in range(self.v)]

        for i in range(self.v):
            if not visited[i]:
                if self.dfs(i, None, visited):
                    return True

        return False


g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)
res = g.detectCycle()
print(res)

g1 = Graph(3)
g1.addEdge(0, 1)
g1.addEdge(1, 2)
res = g1.detectCycle()
print(res)
