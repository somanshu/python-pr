# Minimum steps to reach end of array under constraints
# https://www.geeksforgeeks.org/minimum-steps-reach-end-array-constraints/

from collections import defaultdict


class Graph():
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, fromvtx, tovtx):
        self.graph[fromvtx].append(tovtx)
        self.graph[tovtx].append(fromvtx)


def getDuplicateCollection(arr):
    g = Graph(10)

    for i in range(len(arr)):
        g.graph[arr[i]].append(i)

    return g.graph


def isSafe(i, arr, visited):
    return i >= 0 and i < len(arr) and not visited[i]


def getMinSteps(duplicates, arr):
    visited = [False for i in range(len(arr))]
    queue = []

    queue.append((0, 0))
    visited[0] = True

    while len(queue) > 0:
        (index, d) = queue.pop(0)
        if index == len(arr) - 1:
            return d

        if isSafe(index+1, arr, visited):
            visited[index+1] = True
            queue.append((index+1, d+1))

        if isSafe(index-1, arr, visited):
            visited[index-1] = True
            queue.append((index-1, d+1))

        for i in duplicates[arr[index]]:
            if not visited[i]:
                visited[i] = True
                queue.append((i, d+1))


arr = [0, 1, 2, 3, 4, 5, 6, 7, 5, 4,
       3, 6, 0, 1, 2, 3, 4, 5, 7]
duplicates = getDuplicateCollection(arr)
res = getMinSteps(duplicates, arr)
print(res)
