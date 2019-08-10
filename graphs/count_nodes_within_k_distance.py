# Count nodes within K-distance from all nodes in a set
# https://www.geeksforgeeks.org/count-nodes-within-k-distance-from-all-nodes-in-a-set/

from collections import defaultdict


class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, fromvtx, tovtx):
        self.graph[fromvtx].append(tovtx)
        self.graph[tovtx].append(fromvtx)

    def bfs(self, queueItem, visited, queue, distance):
        (vertex, level) = queueItem

        for i in self.graph[vertex]:
            if not visited[i]:
                visited[i] = True
                distance[i] = level + 1
                queue.append((i, level + 1))

        return

    # returns the furthest marked vertex and all distance from starting vertex
    def getFarthestMarkedNode(self, marked, vtx):
        visited = [False for i in range(self.v)]
        distance = [9999 for i in range(self.v)]
        queue = []
        visited[vtx] = True
        distance[vtx] = 0
        queue.append((vtx, 0))

        while len(queue) > 0:
            queueItem = queue.pop(0)
            self.bfs(queueItem, visited, queue, distance)

        maxDistance = 0
        maxDistanceVtx = None
        for i in range(len(distance)):
            if i not in marked:
                continue

            if distance[i] > maxDistance:
                maxDistance = distance[i]
                maxDistanceVtx = i

        return (maxDistanceVtx, distance)

    def getNodesWithinKDistance(self, distance, vertex, k):
        nodes = []
        dist = [9999 for i in range(self.v)]
        visited = [False for i in range(self.v)]
        queue = []
        queue.append((vertex, 0))

        while len(queue) > 0:
            queueItem = queue.pop(0)

            if queueItem[1] < k:
                self.bfs(queueItem, visited, queue, dist)

        for i in range(self.v):
            if dist[i] <= k and distance[i] <= k:
                nodes.append(i)

        return nodes

    def findAllNodesWithinKDistance(self, marked, k):
        (fmNode, d) = self.getFarthestMarkedNode(marked, 0)
        (smNode, distance) = self.getFarthestMarkedNode(marked, fmNode)
        nodes = self.getNodesWithinKDistance(distance, smNode, k)
        print(nodes)


g = Graph(10)
g.addEdge(1, 0)
g.addEdge(0, 3)
g.addEdge(0, 8)
g.addEdge(2, 3)
g.addEdge(3, 5)
g.addEdge(3, 6)
g.addEdge(3, 7)
g.addEdge(4, 5)
g.addEdge(5, 9)
marked = {1, 2, 4}
k = 3
g.findAllNodesWithinKDistance(marked, k)
