# Given a sorted dictionary of an alien language, find order of characters
# https://www.geeksforgeeks.org/given-sorted-dictionary-find-precedence-characters/

from collections import defaultdict


class Graph():
    def __init__(self, v):
        self.v = v
        self.vertices = {}
        self.graph = defaultdict(list)

    def addEdge(self, fromvtx, tovtx):
        self.graph[fromvtx].append(tovtx)

    def topological_sort(self):
        visited = {}
        for v in self.vertices:
            visited[v] = False
        stack = []

        for i in self.vertices:
            if not visited[i]:
                self.topo_util(i, visited, stack)

        stack.reverse()
        return stack

    def topo_util(self, vertex, visited, stack):
        visited[vertex] = True

        for i in self.graph[vertex]:
            if not visited[i]:
                self.topo_util(i, visited, stack)

        stack.append(vertex)


def createGraph(words, characters):
    n = len(words)
    g = Graph(characters)

    for i in range(n - 1):
        word1 = words[i]
        word2 = words[i+1]
        char1 = None
        char2 = None

        for j in range(min(len(word1), len(word2))):
            char1 = word1[j]
            char2 = word2[j]

            if char1 != char2:
                break

        if char1 != char2:
            g.addEdge(char1, char2)
            g.vertices[char1] = char1
            g.vertices[char2] = char2
            continue

    return g


words = ["baa", "abcd", "abca", "cab", "cad"]
g = createGraph(words, 4)
res = g.topological_sort()
print(res)
