# Minimum edge reversals to make a root
# https://www.geeksforgeeks.org/minimum-edge-reversals-to-make-a-root/


from collections import defaultdict


class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdgeDirected(self, fromvtx, tovtx):
        self.graph[fromvtx].append(tovtx)

    def addEdgeUnDirected(self, fromvtx, tovtx):
        self.graph[fromvtx].append(tovtx)
        self.graph[tovtx].append(fromvtx)

    def getUndirectedGraph(self):
        g = Graph(self.v)

        for i in range(self.v):
            for j in self.graph[i]:
                g.addEdgeUnDirected(i, j)

        return g.graph

    def hasEdge(self, fromvtx, tovtx):
        if tovtx in self.graph[fromvtx]:
            return True

        return False

    def dfs(self, vtx, ungraph, reversal, distance, visited):
        visited[vtx] = True

        for i in ungraph[vtx]:
            if not visited[i]:
                if self.hasEdge(vtx, i):
                    reversal[i] = reversal[vtx]
                else:
                    reversal[i] = reversal[vtx] + 1

                distance[i] = distance[vtx] + 1
                self.dfs(i, ungraph, reversal, distance, visited)

    def find_min_reverse_nodes(self):
        ungraph = self.getUndirectedGraph()
        visited = [False for i in range(self.v)]
        distance = [0 for i in range(self.v)]
        reversal = [0 for i in range(self.v)]

        self.dfs(0, ungraph, reversal, distance, visited)
        minReversals = max(reversal)
        rootVtx = None

        for i in range(self.v):
            if i == 0:
                continue

            diff = distance[i] - reversal[i]
            if diff < reversal[i] and diff < minReversals:
                minReversals = diff
                rootVtx = i

        totalReversals = max(reversal) - reversal[rootVtx] + minReversals
        return (rootVtx, totalReversals)


g = Graph(8)
g.addEdgeDirected(0, 1)
g.addEdgeDirected(2, 1)
g.addEdgeDirected(3, 2)
g.addEdgeDirected(3, 4)
g.addEdgeDirected(5, 4)
g.addEdgeDirected(5, 6)
g.addEdgeDirected(7, 6)

res = g.find_min_reverse_nodes()
print(res)
