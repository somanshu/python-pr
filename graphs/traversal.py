from collections import defaultdict


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, fromVtx, toVtx):
        self.graph[fromVtx].append(toVtx)


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def isEmpty(self):
        return len(self.queue) is 0


def bfsFromVertex(vertex):
    visited = {}

    for v in g.graph:
        visited[v] = None

    queue = Queue()
    queue.enqueue(vertex)
    visited[vertex] = True

    while(not queue.isEmpty()):
        vtx = queue.dequeue()
        print(vtx, end=" ")

        for v in g.graph[vtx]:
            if visited[v]:
                continue

            queue.enqueue(v)
            visited[v] = True


def dfsUtil(vertex, visited):
    visited[vertex] = True
    print(vertex, end=" ")

    for v in g.graph[vertex]:
        if visited[v]:
            continue

        dfsUtil(v, visited)


def dfsFromVertex(vertex):
    visited = {}

    for v in g.graph:
        visited[v] = None

    dfsUtil(vertex, visited)


def dfs():
    visited = {}

    for v in g.graph:
        visited[v] = None

    for v in g.graph:
        if visited[v]:
            continue
        dfsUtil(v, visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

# bfsFromVertex(2)
# dfsFromVertex(2)
dfs()
