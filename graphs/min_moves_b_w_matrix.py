# Find the minimum number of moves needed to move from one cell of matrix to another
# https://www.geeksforgeeks.org/find-minimum-numbers-moves-needed-move-one-cell-matrix-another/

from collections import defaultdict


class Graph():
    def __init__(self, v):
        self.v = v
        self.source = None
        self.destination = None
        self.graph = defaultdict(list)

    def addEdge(self, fromvtx, tovtx):
        self.graph[fromvtx].append(tovtx)
        self.graph[tovtx].append(fromvtx)

    def getMinDistance(self):
        visited = [False for i in range(self.v)]
        queue = []
        queue.append((self.source, 0))
        visited[self.source] = True

        while len(queue) > 0:
            (v, d) = queue.pop(0)

            if v == self.destination:
                return d

            for i in self.graph[v]:
                if not visited[i]:
                    visited[i] = True
                    queue.append((i, d+1))


def isSafe(i, j, n, m):
    return i >= 0 and j >= 0 and i < n and j < n and m[i][j] != 0


def constructGraph(matrix):
    n = len(matrix)
    g = Graph(n*n)
    source = None
    destination = None

    for i in range(n):
        for j in range(n):
            k = i * n + j

            # move left
            if isSafe(i, j-1, n, matrix):
                g.addEdge(k, k-1)

            # move right
            if isSafe(i, j+1, n, matrix):
                g.addEdge(k, k+1)

            # move top
            if isSafe(i-1, j, n, matrix):
                g.addEdge(k, k-n)

            #  move bottom
            if isSafe(i+1, j, n, matrix):
                g.addEdge(k, k+n)

            if matrix[i][j] == 1:
                g.source = k

            if matrix[i][j] == 2:
                g.destination = k

    return g


# mat = [
#     [0, 3, 2],
#     [3, 3, 0],
#     [1, 3, 0]
# ]
# n = 3

mat = [
    [3, 3, 1, 0],
    [3, 0, 3, 3],
    [2, 3, 0, 3],
    [0, 3, 3, 3]
]
n = 4

g = constructGraph(mat)
res = g.getMinDistance()
print(res)
