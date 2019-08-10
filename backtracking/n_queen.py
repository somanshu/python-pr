# https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/


def isValidCoordinate(x, y, n):
    return x >= 0 and y >= 0 and x < n and y < n


def isSafe(x, y, sol, n):
    if not isValidCoordinate(x, y, n):
        return False

    # check rows, columns and diagonals
    for i in range(n):
        if sol[i][y]:
            return False
        if sol[x][i]:
            return False
        if isValidCoordinate(x+i, y+i, n) and sol[x+i][y+i]:
            return False
        if isValidCoordinate(x+i, y-i, n) and sol[x+i][y-i]:
            return False
        if isValidCoordinate(x-i, y+i, n) and sol[x-i][y+i]:
            return False
        if isValidCoordinate(x-i, y-i, n) and sol[x-i][y-i]:
            return False

    return True


def solve_n_queen(queens, row, column, visited, n):
    visited[row][column] = 1
    if queens == 1:
        return True

    for i in range(n):
        if isSafe(row + 1, i, visited, n):
            if solve_n_queen(queens - 1, row + 1, i, visited, n):
                return True

    visited[row][column] = 0
    return False


def n_queen(n):
    visited = [[0 for i in range(n)] for j in range(n)]
    queens = n

    for i in range(n):
        if solve_n_queen(queens, 0, i, visited, n):
            return print_sol(visited)

    return False


def print_sol(sol):
    for item in sol:
        print(item)


n = 4
n_queen(n)
