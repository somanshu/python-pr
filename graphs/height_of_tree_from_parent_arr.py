# Height of a generic tree from parent array
# We are given a tree of size n as array parent[0..n-1]
# where every index i in parent[] represents a node and the value at
# i represents the immediate parent of that node. For root node value will be - 1.
# Find the height of the generic tree given the parent links.

from collections import defaultdict


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, fromVtx, toVtx):
        self.graph[fromVtx].append(toVtx)


def create_graph(parent):
    root = None
    g = Graph()
    for i in range(len(parent)):
        node = i
        parentNode = parent[i]

        if parentNode == -1:
            root = node
            continue

        g.addEdge(parentNode, node)

    return {
        "root": root,
        "graph": g.graph
    }


def bfs(root, graph, nodes):
    queue = []
    visited = [False for i in range(nodes)]
    height = 0

    queue.append((root, 0))
    visited[root] = True

    while len(queue) > 0:
        (node, level) = queue.pop(0)

        if level > height:
            height = level

        for i in graph[node]:
            if not visited[i]:
                queue.append((i, level + 1))

    return height


# parent = [-1, 0, 0, 0, 3, 1, 1, 2]
parent = [-1, 0, 1, 2, 3]
res = create_graph(parent)
res = bfs(res["root"], res["graph"], len(parent))
print(res)
