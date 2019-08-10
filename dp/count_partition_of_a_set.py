# Count number of ways to partition a set into k subsets
# Given two numbers n and k where n represents
# number of elements in a set, find number of ways to partition the set into k subsets.

s = [[-1 for i in range(3)] for j in range(4)]


def partition(n, k, s):
    if s[n][k] >= 0:
        return s[n][k]

    if (n == 0 or k == 0 or k > n):
        s[n][k] = 0
        return s[n][k]

    if (k == 1 or k == n):
        s[n][k] = 1
        return s[n][k]

    s[n][k] = k * partition(n-1, k, s) + partition(n-1, k-1, s)
    return s[n][k]


print(partition(3, 2, s))
