# Count even length binary sequences with same sum of first and second half bits
# https://www.geeksforgeeks.org/count-even-length-binary-sequences-with-same-sum-of-first-and-second-half-bits/


def countSeq1(length, x, y, n):
    if length == 0:
        return 1 if x == y else 0

    count = 0

    count += countSeq1(length - 1, x, y, n)
    count += countSeq1(length - 1, x + 1, y, n)
    count += countSeq1(length - 1, x + 1, y + 1, n)
    count += countSeq1(length - 1, x, y + 1, n)

    return count


def countSeq2(n, diff):
    if abs(diff) > n:
        return 0

    if n == 1 and diff == 0:
        return 2

    if n == 1 and abs(diff) == 1:
        return 1

    return countSeq2(n-1, diff + 1) + countSeq2(n-1, diff - 1) + 2 * countSeq2(n-1, diff)


def countSeq3(n, diff):
    if abs(diff) > n:
        return 0

    if n == 1 and diff == 0:
        return 2

    if n == 1 and abs(diff) == 1:
        return 1

    if (n, diff) in lookup:
        return lookup[(n, diff)]

    lookup[(n, diff)] = countSeq3(n-1, diff + 1) + \
        countSeq3(n-1, diff - 1) + 2 * countSeq3(n-1, diff)
    return lookup[(n, diff)]


lookup = {}
res = countSeq1(3, 0, 0, 3)
res = countSeq3(3, 0)
print(res)
