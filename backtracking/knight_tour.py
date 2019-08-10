# https://www.geeksforgeeks.org/the-knights-tour-problem-backtracking-1/


def isSafe(x, y, visited, n):
    if x >= 0 and y >= 0 and x < n and y < n and visited[x][y] == -1:
        return True

    return False


def solve_knight_tour(x, y, visited, count, n):
    visited[x][y] = count

    if (count == n * n):
        return True

    x_arr = [2, 1, -1, -2, -2, -1,  1,  2]
    y_arr = [1, 2,  2,  1, -1, -2, -2, -1]

    for i in range(len(x_arr)):
        if isSafe(x + x_arr[i], y + y_arr[i], visited, n):
            if solve_knight_tour(x + x_arr[i], y + y_arr[i], visited, count + 1, n):
                return True

    visited[x][y] = -1
    return False


def find_tour(n):
    visited = [[-1 for i in range(n)] for j in range(n)]

    if solve_knight_tour(0, 0, visited, 1, n):
        return visited

    return False


def print_tour(mat):
    for i in mat:
        print(i)


n = 8
res = find_tour(n)
print_tour(res)
