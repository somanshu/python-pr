# Disjoint Set (Or Union-Find) | Set 1 (Detect Cycle in an Undirected Graph)
# https://www.geeksforgeeks.org/union-find/

from collections import defaultdict


class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, fromvtx, tovtx):
        self.graph[fromvtx].append(tovtx)
        self.graph[tovtx].append(fromvtx)

    def findParent(self, v, parent):
        if parent[v] == -1:
            return v

        return self.findParent(parent[v], parent)

    def union(self, x, y, parent):
        x_set = self.findParent(x, parent)
        y_set = self.findParent(y, parent)

        parent[x_set] = y_set

    def detectCycle(self):
        parent = [-1 for i in range(self.v)]

        for i in self.graph:
            for j in self.graph[i]:
                x_set = self.findParent(i, parent)
                y_set = self.findParent(j, parent)

                if x_set == y_set:
                    return True

                self.union(i, j, parent)

        return False


g = Graph(3)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)
res = g.detectCycle()
print(res)
