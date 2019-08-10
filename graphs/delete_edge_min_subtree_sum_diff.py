# Delete Edge to minimize subtree sum difference
# https://www.geeksforgeeks.org/delete-edge-minimize-subtree-sum-difference/

from collections import defaultdict


class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, fromvtx, tovtx):
        self.graph[fromvtx].append(tovtx)
        self.graph[tovtx].append(fromvtx)

    def dfs(self, vertex, parentVtx, subtree, totalWt, res):
        stWt = subtree[vertex]

        for i in self.graph[vertex]:
            if i != parentVtx:
                self.dfs(i, vertex, subtree, totalWt, res)
                stWt += subtree[i]

        subtree[vertex] = stWt

        if vertex != 0 and abs(totalWt - 2 * subtree[vertex]) < res[0]:
            res[0] = abs(totalWt - 2 * subtree[vertex])

    def getMinDiff(self, weights):
        totalWt = 0
        subtree = [weights[i] for i in range(self.v)]

        for i in range(self.v):
            totalWt += weights[i]

        res = [999999]
        self.dfs(0, None, subtree, totalWt, res)
        return res[0]


weights = [4, 2, 1, 6, 3, 5, 2]
v = len(weights)
g = Graph(v)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(2, 4)
g.addEdge(2, 5)
g.addEdge(3, 6)
res = g.getMinDiff(weights)
print(res)
