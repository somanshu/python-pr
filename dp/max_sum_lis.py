# https://www.geeksforgeeks.org/maximum-sum-increasing-subsequence-dp-14/


def max_sum_lis(arr):
    l = arr[:]
    resArr = [[] for i in range(len(arr))]

    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j] and l[i] < l[j] + arr[i]:
                l[i] = l[j] + arr[i]
                resArr[i] = resArr[j][:]

        resArr[i].append(arr[i])

    maxSum = 0
    index = 0
    for i in range(len(l)):
        if l[i] > maxSum:
            maxSum = l[i]
            index = i

    return (maxSum, resArr[index])


arr = [1, 101, 2, 3, 100, 4, 5]
res = max_sum_lis(arr)
print(res)
