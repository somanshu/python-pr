# https://www.geeksforgeeks.org/longest-repeated-subsequence/


def lrs(str1, i, j, lookup):
    if i < 0 or j < 0:
        return 0

    if lookup[i][j]:
        return lookup[i][j]

    if str1[i-1] == str1[j-1] and i != j:
        lookup[i][j] = 1 + lrs(str1, i-1, j-1, lookup)
        return lookup[i][j]

    lookup[i][j] = max(lrs(str1, i, j-1, lookup), lrs(str1, i-1, j, lookup))
    return lookup[i][j]


def printRes(lookup, str1):
    i = len(str1)
    j = len(str1)
    res = ''

    while i > 0 and j > 0:
        if lookup[i][j] == lookup[i-1][j-1] + 1:
            res = str1[i-1] + res
            i -= 1
            j -= 1
        elif lookup[i][j] == lookup[i-1][j]:
            i -= 1
        else:
            j -= 1

    return res


str1 = 'aabebcdd'
lookup = [[0 for i in range(len(str1) + 1)] for j in range(len(str1) + 1)]
res = lrs(str1, len(str1), len(str1), lookup)
print(res)
res = printRes(lookup, str1)
print(res)
