# https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/

from collections import defaultdict


class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, fromvtx, tovtx):
        self.graph[fromvtx].append(tovtx)

    def topological_sort(self):
        indegree = [0 for i in range(self.v)]

        for i in self.graph:
            for j in self.graph[i]:
                indegree[j] += 1

        queue = []
        topo = []
        count = 0
        for i in range(self.v):
            if indegree[i] == 0:
                queue.append(i)

        while len(queue) > 0:
            v = queue.pop(0)
            topo.append(v)

            for i in self.graph[v]:
                indegree[i] -= 1

                if indegree[i] == 0:
                    queue.append(i)

            count += 1

        if count == self.v:
            return topo

        return False


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
res = g.topological_sort()
print(res)
