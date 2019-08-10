# Cycles of length n in an undirected and connected graph
# https://www.geeksforgeeks.org/cycles-of-length-n-in-an-undirected-and-connected-graph/

from collections import defaultdict


class Graph():
    def __init__(self, v, n, count):
        self.v = v
        self.n = n
        self.count = count
        self.graph = defaultdict(list)

    def addEdge(self, fromvtx, tovtx):
        self.graph[fromvtx].append(tovtx)
        self.graph[tovtx].append(fromvtx)

    def dfs(self, vertex, visited, start_vertex, length):
        visited[vertex] = True

        for i in self.graph[vertex]:
            if not visited[i] and length > 1:
                self.dfs(i, visited, start_vertex, length-1)
            elif i == start_vertex and length == 1:
                self.count += 1

        visited[vertex] = False

    def getCycleCount(self):
        visited = [False for i in range(self.v)]
        totalVerticesToTraverse = self.v - self.n + 1

        for i in range(totalVerticesToTraverse):
            self.dfs(i, visited, i, self.n)
            visited[i] = True

        return int(self.count / 2)


g = Graph(5, 4, 0)
g.addEdge(0, 1)
g.addEdge(0, 3)
g.addEdge(1, 2)
g.addEdge(1, 4)
g.addEdge(2, 3)
g.addEdge(3, 4)
res = g.getCycleCount()
print(res)
