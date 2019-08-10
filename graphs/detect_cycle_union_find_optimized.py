from collections import defaultdict


class Subset():
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank


class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def add_edge(self, fromvtx, tovtx):
        self.graph[fromvtx].append(tovtx)

    def findParent(self, x, subsets):
        if subsets[x].parent == x:
            return subsets[x].parent

        subsets[x].parent = self.findParent(subsets[x].parent, subsets)
        return subsets[x].parent

    def union(self, x, y, subsets):
        x_set = self.findParent(x, subsets)
        y_set = self.findParent(y, subsets)

        if subsets[x_set].rank > subsets[y_set].rank:
            subsets[y_set].parent = x_set
        elif subsets[x_set].rank < subsets[y_set].rank:
            subsets[x_set].parent = y_set
        else:
            subsets[y_set].parent = x_set
            subsets[x_set].rank += 1

    def detectCycle(self):
        subsets = [Subset(i, 0) for i in range(self.v)]

        for i in self.graph:
            for j in self.graph[i]:
                x = self.findParent(i, subsets)
                y = self.findParent(j, subsets)

                if x == y:
                    return True

                self.union(x, y, subsets)

        return False


g = Graph(3)

# add edge 0-1
g.add_edge(0, 1)

# add edge 1-2
g.add_edge(1, 2)

# add edge 0-2
g.add_edge(0, 2)
res = g.detectCycle()

print(res)
