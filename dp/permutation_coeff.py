def pc(n, k):
    if k > n:
        return 0

    if k == 0:
        return 1

    if k == 1:
        return n

    res = n
    for i in range(1, k):
        res *= n - i

    return res


print(pc(10, 3))
