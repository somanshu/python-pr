# https: // www.geeksforgeeks.org/given-a-sorted-and-rotated-array-find-if-there-is-a-pair-with-a-given-sum/

import math


def binary_search(arr, left, right):
    if (left >= right):
        return -1

    mid = int(math.floor((left + right) / 2))

    if (arr[mid] > arr[mid + 1]):
        return mid

    if (arr[mid] < arr[right]):
        return binary_search(arr, left, mid - 1)

    binary_search(arr, mid + 1, right)


def find_pivot(arr):
    return binary_search(arr, 0, len(arr) - 1)

# sorted and rotated array


def find_sum(arr, sum):
    n = len(arr)
    pivot = find_pivot(arr)
    left = (pivot + 1) % n
    right = (n + pivot) % n
    count = 0
    pairs = []

    while left != right:
        if sum < arr[left] + arr[right]:
            right = (n + right - 1) % n
            continue
        if sum > arr[left] + arr[right]:
            left = (left + 1) % n
            continue

        pairs.append({left, right})
        count += 1
        right = (n + right - 1) % n

    if (count > 0):
        return pairs

    return -1


arr = [4, 5, 6, 7, 1, 2, 3]
sum = 7
result = find_sum(arr, sum)
print(result)
