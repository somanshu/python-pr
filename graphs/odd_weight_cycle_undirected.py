# Check if there is a cycle with odd weight sum in an undirected graph
# https://www.geeksforgeeks.org/check-if-there-is-a-cycle-with-odd-weight-sum-in-an-undirected-graph/

from collections import defaultdict


class Edge():
    def __init__(self, v1, v2, wt):
        self.v1 = v1
        self.v2 = v2
        self.wt = wt


class Graph():
    def __init__(self, v):
        self.v = v
        self.graph1 = defaultdict(list)
        self.graph2 = []

    def addEdge(self, fromvtx, tovtx):
        self.graph1[fromvtx].append(tovtx)
        self.graph1[tovtx].append(fromvtx)

    def addEdge2(self, edge):
        self.graph2.append(edge)

    def createGraph(self):
        g = Graph(self.v)
        pseudo_v = self.v + 1
        count = 0
        for edge in self.graph2:
            if edge.wt % 2 == 0:
                count += 1
                g.addEdge(edge.v1, pseudo_v)
                g.addEdge(pseudo_v, edge.v2)
            else:
                g.addEdge(edge.v1, edge.v2)

        g.v = self.v + count

        return g

    def check_bipartite(self):
        color = [None for i in range(self.v+1)]
        queue = []
        queue.append(1)
        color[1] = 0

        while len(queue) > 0:
            v = queue.pop(0)

            for i in self.graph1[v]:
                if color[i] == color[v]:
                    return False

                if color[i] == None:
                    color[i] = 1 - color[v]
                    queue.append(i)

        return True


g = Graph(4)
g.addEdge2(Edge(1, 2, 12))
g.addEdge2(Edge(2, 3, 1))
g.addEdge2(Edge(4, 3, 1))
g.addEdge2(Edge(4, 1, 20))
g1 = g.createGraph()
res = g1.check_bipartite()
print(res)
