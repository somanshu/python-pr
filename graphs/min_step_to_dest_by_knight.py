# Minimum steps to reach target by a Knight
# https://www.geeksforgeeks.org/minimum-steps-reach-target-knight/

from collections import defaultdict


class Cell():
    def __init__(self, x, y, dist):
        self.dist = dist
        self.x = x
        self.y = y


def isSafe(i, j, n, visited):
    return i > 0 and j > 0 and i <= n and j <= n and not visited[i][j]


def getMinSteps(n, source, destination):
    visited = [[False for i in range(n+1)] for j in range(n+1)]
    queue = []
    queue.append(source)

    while len(queue) > 0:
        cell = queue.pop(0)

        if cell.x == destination.x and cell.y == destination.y:
            return cell.dist

        if isSafe(cell.x + 2, cell.y + 1, n, visited):
            visited[cell.x + 2][cell.y + 1] = True
            queue.append(Cell(cell.x + 2, cell.y + 1, cell.dist + 1))

        if isSafe(cell.x + 2, cell.y - 1, n, visited):
            visited[cell.x + 2][cell.y - 1] = True
            queue.append(Cell(cell.x + 2, cell.y - 1, cell.dist + 1))

        if isSafe(cell.x - 2, cell.y - 1, n, visited):
            visited[cell.x - 2][cell.y - 1] = True
            queue.append(Cell(cell.x - 2, cell.y - 1, cell.dist + 1))

        if isSafe(cell.x - 2, cell.y + 1, n, visited):
            visited[cell.x - 2][cell.y + 1] = True
            queue.append(Cell(cell.x - 2, cell.y + 1, cell.dist + 1))

        if isSafe(cell.x - 1, cell.y + 2, n, visited):
            visited[cell.x - 1][cell.y + 2] = True
            queue.append(Cell(cell.x - 1, cell.y + 2, cell.dist + 1))

        if isSafe(cell.x - 1, cell.y - 2, n, visited):
            visited[cell.x - 1][cell.y - 2] = True
            queue.append(Cell(cell.x - 1, cell.y - 2, cell.dist + 1))

        if isSafe(cell.x + 1, cell.y + 2, n, visited):
            visited[cell.x + 1][cell.y + 2] = True
            queue.append(Cell(cell.x + 1, cell.y + 2, cell.dist + 1))

        if isSafe(cell.x + 1, cell.y - 2, n, visited):
            visited[cell.x + 1][cell.y - 2] = True
            queue.append(Cell(cell.x + 1, cell.y - 2, cell.dist + 1))


n = 30
source = Cell(1, 1, 0)
destination = Cell(30, 30, 0)
res = getMinSteps(n, source, destination)
print(res)
