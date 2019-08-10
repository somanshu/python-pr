# Shortest path to reach one prime to other by changing single digit at a time

from collections import defaultdict
import math


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, fromVtx, toVtx):
        self.graph[fromVtx].append(toVtx)
        self.graph[toVtx].append(fromVtx)


def get_all_primes():
    isPrime = [True for i in range(10000)]
    isPrime[0] = False
    isPrime[1] = False
    isPrime[2] = True
    update_primes(2, isPrime)

    result = [i if isPrime[i]
              else False for i in range(len(isPrime))]
    result = filter(lambda item: item, result)
    return list(result)


def update_primes(num, isPrime):
    current_num = num
    while (current_num**2 < 10000):
        if (not isPrime[current_num]):
            current_num += 1
            continue
        for j in range(current_num**2, 10000, current_num):
            isPrime[j] = False
        current_num += 1


def diff_by_one_digit(val1, val2):
    cur_diff = 0
    while(val1 != 0):
        digit_val1 = val1 % 10
        digit_val2 = val2 % 10
        val1 = math.floor(val1 / 10)
        val2 = math.floor(val2 / 10)

        if digit_val1 != digit_val2:
            cur_diff += 1
    return cur_diff == 1


def bfs(graph, source, destination, totalNodes):
    queue = []
    visited = [0 for i in range(9999)]
    visited[source] = 1
    queue.append(source)

    while len(queue) > 0:
        item = queue.pop(0)
        for i in graph[item]:
            if not visited[i]:
                visited[i] = visited[item] + 1
                queue.append(i)
            if i == destination:
                return visited[i] - 1


source = 1033
destination = 8179
primes = get_all_primes()
primes = list(filter(lambda num: num >= source and num <= 8179, primes))

# create graph
g = Graph()
for i in range(len(primes)):
    for j in range(i+1, len(primes)):
        if(diff_by_one_digit(primes[i], primes[j])):
            g.addEdge(primes[i], primes[j])


res = bfs(g.graph, source, destination, len(primes))
print(res)
