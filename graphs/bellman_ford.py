# Shortest path and Negative cycle in graph

import math


class Edge():
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


class Graph():
    def __init__(self, v):
        self.v = v
        self.edges = []

    def addEdge(self, source, destination, weight):
        self.edges.append(Edge(source, destination, weight))

    def bellman_ford_check_negative_cycle(self):
        distance = [math.inf for i in range(self.v)]
        source = 0
        distance[source] = 0

        for i in range(self.v-1):
            for edge in self.edges:
                if edge.weight != math.inf and distance[edge.destination] > distance[edge.source] + edge.weight:
                    distance[edge.destination] = distance[edge.source] + edge.weight

        print(distance)
        for edge in self.edges:
            if edge.weight != math.inf and distance[edge.destination] > distance[edge.source] + edge.weight:
                return True

        return False


g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)
res = g.bellman_ford_check_negative_cycle()
print(res)


g1 = Graph(4)
g1.addEdge(0, 1, 1)
g1.addEdge(1, 2, -1)
g1.addEdge(2, 3, -1)
g1.addEdge(3, 0, -1)
res = g1.bellman_ford_check_negative_cycle()
print(res)
