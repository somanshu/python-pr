def candies_util(index, arr, n, res):
    if index == n-1:
        if arr[index - 1] < arr[index]:
            res[index] = arr[index - 1] + 1
            return res[index]
        else:
            res[index] = 1
            return 1

    if index == 0 and arr[index + 1] >= arr[index]:
        res[index] = 1
        return res[index]

    if arr[index + 1] >= arr[index]:
        if arr[index - 1] >= arr[index]:
            res[index] = 1
            return res[index]
        else:
            res[index] = 1 + res[index - 1]
            return res[index]

    res1 = 1 + candies_util(index + 1, arr, n, res)
    res2 = 1

    if index > 0 and arr[index - 1] < arr[index]:
        res2 = 1 + res[index - 1]

    res[index] = max(res1, res2)
    return res[index]


# Complete the candies function below.
def candies(n, arr):
    res = [0 for i in range(n)]

    for i in range(n):
        if res[i] == 0:
            candies_util(i, arr, n, res)

    return res


n = 10
arr = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
res = candies(n, arr)
