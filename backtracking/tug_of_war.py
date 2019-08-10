# https://www.geeksforgeeks.org/tug-of-war/

import math


def allocate_set(arr, index, size1, size2, totalSum, sum1, sum2, minDiff, set1, set2):
    if size1 == 0:
        sum2 = totalSum - sum1
        diff = abs(sum1 - sum2)
        if diff < minDiff[0]:
            minDiff[0] = diff
            minDiff[1] = set1[:]
        return

    if size2 == 0:
        sum1 = totalSum - sum2
        diff = abs(sum1 - sum2)
        if diff < minDiff[0]:
            minDiff[0] = diff
            minDiff[1] = set2[:]
        return

    if size1 > 0 and index < len(arr) - 1:
        set1.append(arr[index])
        allocate_set(arr, index + 1, size1 - 1, size2, totalSum,
                     sum1 + arr[index], sum2, minDiff, set1, set2)
        set1.pop(-1)

    if size2 > 0 and index < len(arr) - 1:
        set2.append(arr[index])
        allocate_set(arr, index + 1, size1, size2 -
                     1, totalSum, sum1, sum2 + arr[index], minDiff, set1, set2)
        set2.pop(-1)


def tug_of_war(arr):
    minDiff = [999999, []]
    n = len(arr)
    size1 = n / 2
    size2 = n / 2
    if n % 2 != 0:
        size1 = math.floor((n + 1) / 2)
        size2 = math.floor((n - 1) / 2)
    allocate_set(arr, 0, size1, size2, sum(arr), 0, 0, minDiff, [], [])
    return minDiff


arr = [23, 45, -34, 12, 0, 98,
       -99, 4, 189, -1, 4]
res = tug_of_war(arr)
print(res)
