# Find k-cores of an undirected graph

from collections import defaultdict


class Graph():
    def __init__(self, vertices):
        self.v = vertices
        self.graph = defaultdict(list)

    def addEdge(self, source, destination):
        self.graph[source].append(destination)
        self.graph[destination].append(source)

# sol1


def dfsUtil1(v, k, mem, graph):
    mem[v]["deleted"] = True

    for i in graph[v]:
        mem[i]["degree"] -= 1

    for i in graph[v]:
        if (not mem[i]["deleted"] and mem[i]["degree"] < k):
            dfsUtil1(i, k, mem, graph)


def findKCores1(graph, k):
    mem = defaultdict(dict)

    for i in graph:
        mem[i] = {
            "deleted": False,
            "degree": len(graph[i])
        }

    for i in graph:
        if (not mem[i]["deleted"] and mem[i]["degree"] < k):
            dfsUtil1(i, k, mem, graph)

    return mem


def printKCores1(res, graph):
    coreGraph = defaultdict(list)
    for i in res:
        if res[i]["deleted"]:
            continue

        for j in graph[i]:
            if not res[j]["deleted"]:
                coreGraph[i].append(j)

    return coreGraph


# sol2

def dfsUtil2(v, k, degreeV, visited, graph):
    visited[v] = True

    for i in graph[v]:
        if degreeV[v] < k:
            degreeV[i] -= 1

        if not visited[i]:
            if dfsUtil2(i, k, degreeV, visited, graph):
                degreeV[v] -= 1

    return degreeV[v] < k


def findKCores2(graph, v, k):
    visited = [False for i in range(v)]
    degreeV = [0 for i in range(v)]

    for i in graph:
        degreeV[i] = len(graph[i])

    dfsUtil2(0, k, degreeV, visited, graph)

    for i in range(v):
        if not visited[i]:
            dfsUtil2(i, k, degreeV, visited, graph)

    return degreeV


k = 3
g1 = Graph(9)
g1.addEdge(0, 1)
g1.addEdge(0, 2)
g1.addEdge(1, 2)
g1.addEdge(1, 5)
g1.addEdge(2, 3)
g1.addEdge(2, 4)
g1.addEdge(2, 5)
g1.addEdge(2, 6)
g1.addEdge(3, 4)
g1.addEdge(3, 6)
g1.addEdge(3, 7)
g1.addEdge(4, 6)
g1.addEdge(4, 7)
g1.addEdge(5, 6)
g1.addEdge(5, 8)
g1.addEdge(6, 7)
g1.addEdge(6, 8)

g2 = Graph(13)
g2.addEdge(0, 1)
g2.addEdge(0, 2)
g2.addEdge(0, 3)
g2.addEdge(1, 4)
g2.addEdge(1, 5)
g2.addEdge(1, 6)
g2.addEdge(2, 7)
g2.addEdge(2, 8)
g2.addEdge(2, 9)
g2.addEdge(3, 10)
g2.addEdge(3, 11)
g2.addEdge(3, 12)
res = findKCores2(g1.graph, g1.v, k)
print(res)
# print(printKCores1(res, g2.graph))
