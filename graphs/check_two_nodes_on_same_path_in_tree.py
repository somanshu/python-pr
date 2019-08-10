# Check if two nodes are on same path in a tree
# https://www.geeksforgeeks.org/check-if-two-nodes-are-on-same-path-in-a-tree/

from collections import defaultdict


class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)
        self.timer = 0
        self.intime = [0 for i in range(self.v+1)]
        self.outtime = [0 for i in range(self.v+1)]

    def addEdge(self, fromvtx, tovtx):
        self.graph[fromvtx].append(tovtx)
        self.graph[tovtx].append(fromvtx)

    def dfs(self, vertex, visited):
        self.timer += 1
        visited[vertex] = True
        self.intime[vertex] = self.timer

        for i in self.graph[vertex]:
            if not visited[i]:
                self.dfs(i, visited)

        self.timer += 1
        self.outtime[vertex] = self.timer

    def check_path(self, root):
        visited = [False for i in range(self.v+1)]
        self.dfs(root, visited)

    def isSamePath(self, i, j):
        return (self.intime[i] < self.intime[j]
                and self.outtime[i] > self.outtime[j]) or \
            (self.intime[i] > self.intime[j]
             and self.outtime[i] < self.outtime[j])


g = Graph(9)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(3, 6)
g.addEdge(2, 4)
g.addEdge(2, 5)
g.addEdge(5, 7)
g.addEdge(5, 8)
g.addEdge(5, 9)

g.check_path(1)
res = g.isSamePath(2, 9)
print(res)
