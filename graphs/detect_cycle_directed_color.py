# Detect Cycle in a directed graph using colors
# https://www.geeksforgeeks.org/detect-cycle-direct-graph-using-colors/

# White - initial state
# Grey - in progress(recursion)
# black - recursion complete

from collections import defaultdict


class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, fromvtx, tovtx):
        self.graph[fromvtx].append(tovtx)

    def dfs_color(self, vertex, colors):
        colors[vertex] = 'GREY'

        for i in self.graph[vertex]:
            if colors[i] == 'WHITE':
                if self.dfs_color(i, colors):
                    return True
            elif colors[i] == 'GREY':
                return True

        colors[vertex] = 'BLACK'
        return False

    def detectCycle(self):
        colors = ['WHITE' for i in range(self.v)]

        for i in range(self.v):
            if colors[i] == 'WHITE':
                if self.dfs_color(i, colors):
                    return True

        return False


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
res = g.detectCycle()
print(res)

g1 = Graph(3)
g1.addEdge(0, 1)
g1.addEdge(0, 2)
g1.addEdge(1, 2)
res = g1.detectCycle()
print(res)
