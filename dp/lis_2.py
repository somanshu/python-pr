
def lis(arr):
    lookup = [1 for i in range(len(arr))]
    resArr = [[] for i in range(len(arr))]
    resArr[0].append(arr[0])

    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j] and lookup[i] < lookup[j] + 1:
                lookup[i] = lookup[j] + 1
                resArr[i] = resArr[j][:]

        resArr[i].append(arr[i])

    maxLength = 0
    solArr = None
    for res in resArr:
        if len(res) > maxLength:
            maxLength = len(res)
            solArr = res

    return (maxLength, solArr)


arr = [10, 22, 9, 33, 21, 50, 41, 60]
(length, solArr) = lis(arr)
print(length, solArr)
