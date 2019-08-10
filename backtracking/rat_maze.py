# https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/


def isSafe(x, y, visited, mat):
    return x >= 0 and y >= 0 and x < len(mat) and y < len(mat[0]) and mat[x][y] == 1


def solve_rat_maze(x, y, visited, mat):
    visited[x][y] = True

    if x == len(mat) - 1 and y == len(mat[0]) - 1:
        return True

    # right
    if isSafe(x, y+1, visited, mat):
        if solve_rat_maze(x, y+1, visited, mat):
            return True

    # down
    if isSafe(x+1, y, visited, mat):
        if solve_rat_maze(x+1, y, visited, mat):
            return True

    visited[x][y] = False
    return False


def print_path(res):
    if not res:
        return False

    for item in res:
        print(item)


def find_path(mat):
    visited = [[False for i in range(len(mat[0]))] for j in range(len(mat))]
    res = solve_rat_maze(0, 0, visited, mat)

    if res:
        print_path(visited)


mat = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]
find_path(mat)
