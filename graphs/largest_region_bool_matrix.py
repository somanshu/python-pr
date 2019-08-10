# Find length of the largest region in Boolean Matrix
# https://www.geeksforgeeks.org/find-length-largest-region-boolean-matrix/


def isSafe(x, y, mat):
    return x >= 0 and y >= 0 and x < len(mat) and y < len(mat[0]) and mat[x][y]


def getRegionSize(x, y, mat, visited):
    visited[x][y] = True
    count = 1
    arr = [-1, 0, 1]

    for i in arr:
        for j in arr:
            if isSafe(x+i, y+j, mat) and not visited[x+i][y+j]:
                count += getRegionSize(x+i, y+j, mat, visited)

    return count


def maxRegionSize(mat):
    rows = len(mat)
    colms = len(mat[0])
    visited = [[False for i in range(colms)]
               for j in range(rows)]
    maxCount = 0

    for i in range(rows):
        for j in range(colms):
            if mat[i][j] and not visited[i][j]:
                count = getRegionSize(i, j, mat, visited)
                if count > maxCount:
                    maxCount = count

    return maxCount


mat = [
    [0, 0, 1, 1, 0],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1]
]
res = maxRegionSize(mat)
print(res)
