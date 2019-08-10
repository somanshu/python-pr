# https://www.geeksforgeeks.org/k-maximum-sums-non-overlapping-contiguous-sub-arrays/


def largestSumWithIndices(arr):
    cur_sum = 0
    max_sum = -float("inf")
    start = 0
    end = 0
    s = 0

    for i in range(len(arr)):
        cur_sum += arr[i]

        if cur_sum > max_sum:
            max_sum = cur_sum
            start = s
            end = i

        if cur_sum < 0:
            cur_sum = 0
            s = i + 1

    return (start, end, max_sum)


def k_max(arr, k):
    for i in range(k):
        (s, e, max_sum) = largestSumWithIndices(arr)

        print((s, e, max_sum))

        for j in range(s, e + 1):
            arr[j] = -float("inf")


arr = [4, 1, 1, -1, -3, -5, 6, 2, -6, -2]
k = 3
k_max(arr, k)
