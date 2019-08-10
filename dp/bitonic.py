# inc then dec


def bitonic(arr):
    inc = arr[:]
    incArr = [[] for i in range(len(arr))]

    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j] and inc[i] < inc[j] + arr[i]:
                inc[i] = inc[j] + arr[i]
                incArr[i] = incArr[j][:]
        incArr[i].append(arr[i])

    dec = arr[:]
    decArr = [[] for i in range(len(arr))]

    for i in range(1, len(arr) + 1):
        for j in range(1, i):
            if arr[-i] > arr[-j] and dec[-i] < dec[-j] + arr[-i]:
                dec[-i] = dec[-j] + arr[-i]
                decArr[-i] = decArr[-j][:]
        decArr[-i].insert(0, arr[-i])

    maxSum = 0
    solIndex = 0
    for i in range(len(arr)):
        if inc[i] + dec[i] - arr[i] > maxSum:
            maxSum = inc[i] + dec[i] - arr[i]
            solIndex = i

    solArr = incArr[solIndex][:] + decArr[solIndex][1:]
    return (maxSum, solArr)


arr = [1, 15, 51, 45, 33, 100, 12, 18, 9]
(tsum, resArr) = bitonic(arr)
print(tsum, resArr)
