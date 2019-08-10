# Bell Numbers (Number of ways to Partition a Set)


def partition(n, k, s):
    if s[n][k] != -1:
        return s[n][k]

    if (n == 0 or k == 0 or k > n):
        s[n][k] = 0
        return 0

    if (k == 1 or k == n):
        s[n][k] = 1
        return 1

    s[n][k] = k * partition(n-1, k, s) + partition(n-1, k-1, s)
    return s[n][k]


def bell_number_1(n):
    res = 0

    for i in range(1, n+1):
        s = [[-1 for i in range(i+1)] for j in range(n+1)]
        res += partition(n, i, s)

    return res


def bell_number_2(i, j):
    if i == j and j == 1:
        return 1

    if j == 1:
        return bell_number_2(i-1, i-1)

    return bell_number_2(i, j-1) + bell_number_2(i-1, j-1)


def bell_number_3(i, j, bell):
    if bell[i][j] > 0:
        return bell[i][j]

    if i == j and j == 1:
        bell[i][j] = 1
        return 1

    if j == 1:
        bell[i][j] = bell_number_3(i-1, i-1, bell)
        return bell[i][j]

    bell[i][j] = bell_number_3(i, j-1, bell) + bell_number_3(i-1, j-1, bell)
    return bell[i][j]


# print(bell_number_1(6))
bell = [[0 for i in range(7)] for j in range(7)]
print(bell_number_3(6, 6, bell))
