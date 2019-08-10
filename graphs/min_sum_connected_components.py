# Sum of the minimum elements in all connected components of an undirected graph
# https://www.geeksforgeeks.org/sum-of-the-minimum-elements-in-all-connected-components-of-an-undirected-graph/

from collections import defaultdict


class Min():
    def __init__(self, value, vertex):
        self.value = value
        self.vertex = vertex


class Graph():
    def __init__(self, v, value):
        self.v = v
        self.value = value
        self.graph = defaultdict(list)

    def addEdge(self, fromvtx, tovtx):
        self.graph[fromvtx].append(tovtx)
        self.graph[tovtx].append(fromvtx)

    def bfs(self, vertex, visited, minNode):
        queue = []
        queue.append(vertex)
        visited[vertex] = True

        while len(queue) > 0:
            v = queue.pop(0)
            if self.value[v-1] < minNode.value:
                minNode.value = value[v-1]
                minNode.vertex = v
            for i in self.graph[v]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)

    def getMinByBfs(self):
        visited = [False for i in range(self.v + 1)]
        mins = []

        for i in range(1, self.v + 1):
            if not visited[i]:
                minNode = Min(self.value[i-1], i)
                self.bfs(i, visited, minNode)
                mins.append(minNode)

        minSum = 0
        for item in mins:
            minSum += item.value

        return minSum

    def dfs(self, vertex, visited, minNode):
        visited[vertex] = True
        if self.value[vertex-1] < minNode.value:
            minNode.value = self.value[vertex-1]
            minNode.vertex = vertex

        for i in self.graph[vertex]:
            if not visited[i]:
                self.dfs(i, visited, minNode)

    def getMinByDfs(self):
        visited = [False for i in range(self.v + 1)]
        mins = []

        for i in range(1, self.v + 1):
            if not visited[i]:
                minNode = Min(self.value[i-1], i)
                self.dfs(i, visited, minNode)
                mins.append(minNode)

        minSum = 0
        for item in mins:
            minSum += item.value

        return minSum


value = [1, 6, 2, 7, 3, 8, 4, 9, 5, 10]
g = Graph(len(value), value)

g.addEdge(1, 2)
g.addEdge(3, 4)
g.addEdge(5, 6)
g.addEdge(7, 8)
g.addEdge(9, 10)

res = g.getMinByDfs()
print(res)
