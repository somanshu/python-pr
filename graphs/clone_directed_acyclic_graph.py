from collections import defaultdict


class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, fromvtx, tovtx):
        self.graph[fromvtx].append(tovtx)

    def clone(self):
        queue = []
        visited = [False for i in range(self.v)]
        # node and prev_node
        queue.append((0, None))
        g = Graph(self.v)

        while len(queue) > 0:
            (v, prev_v) = queue.pop(0)
            if prev_v != None:
                g.addEdge(prev_v, v)

            if visited[v]:
                continue

            visited[v] = True

            for i in self.graph[v]:
                if not visited[i]:
                    queue.append((i, v))

        return g


g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(2, 3)
g.addEdge(3, 4)
g1 = g.clone()
print(g1.graph)
