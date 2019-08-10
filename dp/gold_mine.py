# Given a gold mine of n*m dimensions. Each field in this mine contains a
# positive integer which is the amount of gold in tons. Initially the miner
# is at first column but can be at any row. He can move only (right->,right up /,right down\)
# that is from a given cell, the miner can move to the cell diagonally up towards the
# right or right or diagonally down towards the right. Find out maximum amount of gold he can collect.


def getValue(i, j, maxI, maxJ, mine):
    if i > maxI or j > maxJ or i < 0:
        return {"val": 0, "path": ""}

    if j == maxJ:
        return {"val": mat[i][j], "path": f"({i}, {j})"}

    val1 = getValue(i, j+1, maxI, maxJ, mine)
    val2 = getValue(i-1, j+1, maxI, maxJ, mine)
    val3 = getValue(i+1, j+1, maxI, maxJ, mine)
    maxVal = max(val1["val"], val2["val"], val3["val"])

    maxPath = ""

    if maxVal == val1["val"]:
        maxPath = val1["path"]
    elif maxVal == val2["val"]:
        maxPath = val2["path"]
    else:
        maxPath = val3["path"]
    return {"val": mine[i][j] + maxVal, "path": f"{maxPath}, ({i}, {j})"}


def getMaxGoldMined(n, m, mine):
    maxGold = {
        "val": 0,
        "path": ""
    }

    for i in range(n):
        goldMined = getValue(i, 0, n-1, m-1, mine)
        if goldMined["val"] > maxGold["val"]:
            maxGold = goldMined

    return maxGold


# mat = [
#     [1, 3, 3],
#     [2, 1, 4],
#     [0, 6, 4]
# ]

# mat = [
#     [1, 3, 1, 5],
#     [2, 2, 4, 1],
#     [5, 0, 2, 3],
#     [0, 6, 1, 2]
# ]

mat = [
    [10, 33, 13, 15],
    [22, 21, 4, 1],
    [5, 0, 2, 3],
    [0, 6, 14, 2]
]

res = getMaxGoldMined(4, 4, mat)
print(res["val"])
print(res["path"])
