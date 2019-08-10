# Bidirectional Search

from collections import defaultdict


class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, fromvtx, tovtx):
        self.graph[fromvtx].append(tovtx)
        self.graph[tovtx].append(fromvtx)

    def bfs(self, vertex, queue, visited, parent):
        for i in self.graph[vertex]:
            if not visited[i]:
                visited[i] = True
                parent[i] = vertex
                queue.append(i)

    def isIntersecting(self, srcVisited, destVisited):
        for i in range(self.v):
            if srcVisited[i] and destVisited[i]:
                return i

        return None

    def getPath(self, vtx, srcParent, destParent):
        path = [vtx]
        parent = srcParent[vtx]

        while parent != None:
            path.insert(0, parent)
            parent = srcParent[parent]

        parent = destParent[vtx]

        while parent != None:
            path.append(parent)
            parent = destParent[parent]

        return path

    def biDirectionalSearch(self, source, destination):
        srcVisited = [False for i in range(self.v)]
        destVisited = [False for i in range(self.v)]
        srcParent = [None for i in range(self.v)]
        destParent = [None for i in range(self.v)]
        intersect = None
        srcQueue = []
        destQueue = []
        srcQueue.append(source)
        srcVisited[source] = True
        destQueue.append(destination)
        destVisited[destination] = True

        while len(srcQueue) > 0 and len(destQueue) > 0:
            intersect = self.isIntersecting(srcVisited, destVisited)
            if intersect != None:
                break
            srcQueueVtx = srcQueue.pop(0)
            destQueueVtx = destQueue.pop(0)
            self.bfs(srcQueueVtx, srcQueue, srcVisited, srcParent)
            self.bfs(destQueueVtx, destQueue, destVisited, destParent)

        if len(srcQueue) == 0 or len(destQueue) == 0:
            return None

        return self.getPath(intersect, srcParent, destParent)


g = Graph(15)
g.addEdge(0, 4)
g.addEdge(1, 4)
g.addEdge(2, 5)
g.addEdge(3, 5)
g.addEdge(4, 6)
g.addEdge(5, 6)
g.addEdge(6, 7)
g.addEdge(7, 8)
g.addEdge(8, 9)
g.addEdge(8, 10)
g.addEdge(9, 11)
g.addEdge(9, 12)
g.addEdge(10, 13)
g.addEdge(10, 14)

source = 0
destination = 14

res = g.biDirectionalSearch(0, 14)
print(res)
