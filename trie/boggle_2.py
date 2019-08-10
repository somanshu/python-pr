# dfs approach


dictionary = ["GEEKS", "FOR", "QUIZ", "GEE"]
boggle = [
    ['G', 'I', 'Z'],
    ['U', 'E', 'K'],
    ['Q', 'S', 'E']
]


def insideDic(string):
    for word in dictionary:
        if word == string:
            return True

    return False


def findWord(row, col, arr, visited, strRes):
    visited[row][col] = True

    if insideDic(strRes):
        print(strRes)

    for i in range(-1, 2):
        for j in range(-1, 2):
            r = row + i
            c = col + j

            if r >= 0 and c >= 0 and r < len(arr) and c < len(arr[0]) and not visited[r][c]:
                findWord(r, c, arr, visited, strRes + arr[r][c])

    visited[row][col] = False


def doBoggle(arr):
    visited = [[False for i in range(len(arr[0]))] for j in range(len(arr))]

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            findWord(i, j, arr, visited, arr[i][j])


doBoggle(boggle)
