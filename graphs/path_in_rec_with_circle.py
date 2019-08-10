# Path in a Rectangle with Circles
import math


def is_in_circle(x, y, ctr_x, ctr_y, radius):
    diffX = (ctr_x - x) ** 2
    diffY = (ctr_y - y) ** 2
    return math.sqrt(diffX + diffY) <= radius


def mark_point_in_circle(mark, radius, x, y):
    for i in range(1, radius+1):
        left = y - i
        if left >= 0:
            mark[x][left] = True

        right = y + i
        if right < len(mark[0]):
            mark[x][right] = True

        top = x - i
        if top >= 0:
            mark[top][y] = True

        bottom = x + i
        if bottom < len(mark):
            mark[bottom][y] = True

    # diagonals
    for i in range(1, radius):
        top_left_x = x - i
        top_left_y = y - i

        if top_left_x >= 0 and top_left_y >= 0 and is_in_circle(top_left_x, top_left_y, x, y, radius):
            mark[top_left_x][top_left_y] = True

        top_right_x = x - i
        top_right_y = y + i

        if top_right_x >= 0 and top_right_y < len(mark[0]) and is_in_circle(top_right_x, top_right_y, x, y, radius):
            mark[top_right_x][top_right_y] = True

        bottom_right_x = x + i
        bottom_right_y = y + i

        if bottom_right_x < len(mark) and bottom_right_y < len(mark[0]) and is_in_circle(bottom_right_x, bottom_right_y, x, y, radius):
            mark[bottom_right_x][bottom_right_y] = True

        bottom_left_x = x + i
        bottom_left_y = y - i

        if bottom_left_x < len(mark) and bottom_left_y >= 0 and is_in_circle(bottom_left_x, bottom_left_y, x, y, radius):
            mark[bottom_left_x][bottom_left_y] = True


def mark_points_in_circle(mark, radius, centers):
    for center in centers:
        x = center[0]
        y = center[1]
        mark[x][y] = True
        mark_point_in_circle(mark, radius, x, y)


def traverse_path(i, j, destX, destY, visited, mark):
    visited[i][j] = True

    if i == destX and j == destY:
        return True

    res = False

    # top
    if i > 0 and not visited[i-1][j] and not mark[i-1][j]:
        res = traverse_path(i-1, j, destX, destY, visited, mark)
        if res:
            return res

    # top-left
    if i > 0 and j > 0 and not visited[i-1][j-1] and not mark[i-1][j-1]:
        res = traverse_path(i-1, j-1, destX, destY, visited, mark)
        if res:
            return res

    # top-right
    if i > 0 and j < len(mark[0]) - 1 and not visited[i-1][j+1] and not mark[i-1][j+1]:
        res = traverse_path(i-1, j+1, destX, destY, visited, mark)
        if res:
            return res

    # left
    if j > 0 and not visited[i][j-1] and not mark[i][j-1]:
        res = traverse_path(i, j-1, destX, destY, visited, mark)
        if res:
            return res

    # right
    if j < len(mark[0]) - 1 and not visited[i][j+1] and not mark[i][j+1]:
        res = traverse_path(i, j+1, destX, destY, visited, mark)
        if res:
            return res

    # bottom
    if i < len(mark) - 1 and not visited[i+1][j] and not mark[i+1][j]:
        res = traverse_path(i+1, j, destX, destY, visited, mark)
        if res:
            return res

    # bottom-left
    if i < len(mark) - 1 and j > 0 and not visited[i+1][j-1] and not mark[i+1][j-1]:
        res = traverse_path(i+1, j-1, destX, destY, visited, mark)
        if res:
            return res

    # bottom-right
    if i < len(mark) - 1 and j < len(mark[0]) - 1 and not visited[i+1][j+1] and not mark[i+1][j+1]:
        res = traverse_path(i+1, j+1, destX, destY, visited, mark)

    return res


m, n = 5, 5
k = 2
r = 1
centers = [
    [0, 0],
    [1, 2]
]
mark = [[False for i in range(n)] for j in range(m)]
visited = [[False for i in range(n)] for j in range(m)]
mark_points_in_circle(mark, r, centers)
res = traverse_path(0, 0, 4, 4, visited, mark)
print(res)
