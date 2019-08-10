# Number of pair of positions in matrix which are not accessible
# https://www.geeksforgeeks.org/number-pair-positions-matrix-not-accessible/

from collections import defaultdict


class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, fromvtx, tovtx):
        self.graph[fromvtx].append(tovtx)
        self.graph[tovtx].append(fromvtx)

    def dfs(self, vertex, visited, res):
        visited[vertex] = True
        res[0] += 1

        for i in self.graph[vertex]:
            if not visited[i]:
                self.dfs(i, visited, res)


def construct_graph(n, paths):
    g = Graph(n*n)

    for path in paths:
        fromPoint = path[0]
        toPoint = path[1]
        fromNode = (fromPoint[0] - 1) * n + fromPoint[1]
        toNode = (toPoint[0] - 1) * n + toPoint[1]
        g.addEdge(fromNode, toNode)

    return g


def getNonReachablePairs(n, paths):
    g = construct_graph(n, paths)
    visited = [False for i in range(n*n + 1)]
    totalPairs = 0

    for i in range(1, n*n + 1):
        if not visited[i]:
            count = [0]
            g.dfs(i, visited, count)
            totalPairs += count[0] * (n * n - count[0])

    return totalPairs


n = 2
paths = [
    ((1, 1), (1, 2)),
    ((1, 2), (2, 2))
]

res = getNonReachablePairs(n, paths)
print(res)
