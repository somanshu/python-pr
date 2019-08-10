# https://www.geeksforgeeks.org/sequences-given-length-every-element-equal-twice-previous/

import math

lookup = {}


def count_seq(prev_num, m, n):
    if n == 0:
        return 1 if prev_num <= m else 0

    if (prev_num, n) in lookup:
        return lookup[(prev_num, n)]

    count = 0
    for i in range(2 * prev_num, math.floor(m / n) + 1):
        count += count_seq(i, m, n-1)

    lookup[(prev_num, n)] = count
    return count


def getCount(m, n):
    count = 0

    for i in range(1, math.floor(m/n) + 1):
        count += count_seq(i, m, n - 1)

    return count


res = getCount(5, 2)
print(res)
