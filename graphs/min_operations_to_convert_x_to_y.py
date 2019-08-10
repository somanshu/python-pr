# Minimum number of operation required to convert number x into y
# https://www.geeksforgeeks.org/minimum-number-operation-required-convert-number-x-y/

# Multiply number by 2.
# Subtract 1 from the number.

from collections import defaultdict


class Graph():
    # def __init__(self, v):
    #     self.v = v
    #     self.graph = defaultdict(list)

    # def addEdge(self, fromvtx, tovtx):
    #     self.graph[fromvtx].append(tovtx)
    #     self.graph[tovtx].append(fromvtx)

    def getMinSteps(self, source, destination):
        visited = {}
        queue = []
        queue.append((source, 0))
        visited[source] = True

        while len(queue) > 0:
            (v, d) = queue.pop(0)
            if v == destination:
                return d

            if v < destination and v*2 not in visited:
                visited[v*2] = True
                queue.append((v*2, d+1))

            if v > 0 and v-1 not in visited:
                visited[v-1] = True
                queue.append((v-1, d+1))

        return None


g = Graph()
res = g.getMinSteps(2, 5)
print(res)
