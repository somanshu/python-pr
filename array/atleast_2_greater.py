def getSecondMax(arr):
    first = arr[0]
    second = -1

    for i in range(1, len(arr)):
        if arr[i] > first:
            second = first
            first = arr[i]

        elif arr[i] > second:
            second = arr[i]

    return (first, second)


def getElementsWithAtleast2Greater(arr):
    (first, second) = getSecondMax(arr)
    res = []

    for i in range(len(arr)):
        if arr[i] < second:
            res.append(arr[i])

    return res


arr = [7, -2, 3, 4, 9, -1]
res = getElementsWithAtleast2Greater(arr)
print(res)
