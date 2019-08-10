# Clone undirected graph
# https://www.geeksforgeeks.org/clone-an-undirected-graph/

from collections import defaultdict


class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, fromvtx, tovtx):
        self.graph[fromvtx].append(tovtx)
        self.graph[tovtx].append(fromvtx)

    def cloneByBfs(self):
        g = Graph(self.v)
        visited = [False for i in range(self.v)]

        for i in range(self.v):
            if not visited[i]:
                self.bfs(i, visited, g)

        return g

    def bfs(self, vertex, visited, g):
        queue = []
        # vertex and prev vertex
        queue.append((vertex, None))
        visited[vertex] = True

        while len(queue) > 0:
            (v, prev_v) = queue.pop(0)
            visited[v] = True
            if prev_v != None:
                g.addEdge(v, prev_v)

            for i in self.graph[v]:
                if not visited[i]:
                    queue.append((i, v))


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 3)
g.addEdge(1, 2)
g.addEdge(2, 3)

res = g.cloneByBfs()
print(res.graph)
