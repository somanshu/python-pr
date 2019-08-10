# Longest commeon sequence


def lcs(i, j, str1, str2, lookup):
    if i <= 0 or j <= 0:
        return 0

    if lookup[i][j] > 0:
        return lookup[i][j]

    if str1[i-1] == str2[j-1]:
        lookup[i][j] = 1 + lcs(i-1, j-1, str1, str2, lookup)
        return lookup[i][j]

    lookup[i][j] = max(lcs(i-1, j, str1, str2, lookup),
                       lcs(i, j-1, str1, str2, lookup))
    return lookup[i][j]


def printString(lookup, str1, str2):
    i = len(str1)
    j = len(str2)
    res = ''

    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            res = str1[i-1] + res
            i -= 1
            j -= 1
            continue

        if lookup[i-1][j] > lookup[i][j-1]:
            i -= 1
        else:
            j -= 1

    return res


str1 = 'ABCDGH'
str2 = 'AEDFHR'
n = max(len(str1), len(str2))
lookup = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]
print(lcs(len(str1), len(str2), str1, str2, lookup))

res = printString(lookup, str1, str2)
print(res)
