# https://www.geeksforgeeks.org/?p=26604/


class Edge():
    def __init__(self, v1, v2, wt):
        self.v1 = v1
        self.v2 = v2
        self.wt = wt


class Subset():
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank


class Graph():
    def __init__(self, v):
        self.v = v
        self.edges = []

    def addEdge(self, edge):
        self.edges.append(edge)

    def findParent(self, vertex, subsets):
        if subsets[vertex].parent == vertex:
            return subsets[vertex].parent

        subsets[vertex].parent = self.findParent(
            subsets[vertex].parent, subsets)
        return subsets[vertex].parent

    def union(self, v1, v2, subsets):
        v1_parent = self.findParent(v1, subsets)
        v2_parent = self.findParent(v2, subsets)

        if subsets[v1_parent].rank < subsets[v2_parent].rank:
            subsets[v1_parent].parent = v2_parent
        elif subsets[v1_parent].rank > subsets[v2_parent].rank:
            subsets[v2_parent].parent = v1_parent
        else:
            subsets[v2_parent].parent = v1_parent
            subsets[v1_parent].rank += 1

    def kruskal(self):
        g = Graph(self.v)
        subsets = [Subset(i, 0) for i in range(self.v)]
        self.edges.sort(key=lambda x: x.wt)

        for edge in self.edges:
            v1_parent = self.findParent(edge.v1, subsets)
            v2_parent = self.findParent(edge.v2, subsets)

            if v1_parent != v2_parent:
                g.addEdge(edge)
                self.union(v1_parent, v2_parent, subsets)

            if len(g.edges) == self.v - 1:
                break

        return g


g = Graph(9)
g.addEdge(Edge(0, 1, 4))
g.addEdge(Edge(0, 7, 8))
g.addEdge(Edge(1, 2, 8))
g.addEdge(Edge(1, 7, 11))
g.addEdge(Edge(2, 3, 7))
g.addEdge(Edge(2, 5, 4))
g.addEdge(Edge(2, 8, 2))
g.addEdge(Edge(3, 4, 9))
g.addEdge(Edge(3, 5, 14))
g.addEdge(Edge(4, 5, 10))
g.addEdge(Edge(5, 6, 2))
g.addEdge(Edge(6, 7, 1))
g.addEdge(Edge(6, 8, 6))
g.addEdge(Edge(7, 8, 7))
res = g.kruskal()

g = Graph(4)
g.addEdge(Edge(0, 1, 10))
g.addEdge(Edge(0, 2, 6))
g.addEdge(Edge(0, 3, 5))
g.addEdge(Edge(1, 3, 15))
g.addEdge(Edge(2, 3, 4))
res = g.kruskal()
print(res)
