def lis(arr, cur, prev, lookup):
    if cur < 0:
        return 1

    if prev == None:
        return lis(arr, cur - 1, cur, lookup)

    if lookup[cur][prev] > 0:
        return lookup[cur][prev]
    res1 = 0
    res2 = 0
    res3 = 0

    # include current
    if arr[cur] < arr[prev]:
        res1 = 1 + lis(arr, cur - 1, cur, lookup)

    res2 = lis(arr, cur - 1, prev, lookup)
    res3 = lis(arr, cur - 1, None, lookup)

    lookup[cur][prev] = max(res1, res2, res3)
    return lookup[cur][prev]


arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
arr = [3, 10, 2, 1, 20]
arr = [50, 3, 10, 7, 40, 80]
arr = [10, 22, 9, 33, 21, 50, 41, 60]
lookup = [[0 for i in range(len(arr))] for j in range(len(arr))]
res = lis(arr, len(arr) - 1, None, lookup)
print(res)
