# https://www.geeksforgeeks.org/positive-elements-at-even-and-negative-at-odd-positions-relative-order-not-maintained/


def rearrange(arr):
    newarr = [None] * len(arr)
    even = 0
    odd = 1

    for i in range(len(arr)):
        if arr[i] > 0 and even < len(arr):
            newarr[even] = arr[i]
            even += 2
            continue

        if arr[i] > 0:
            newarr[odd] = arr[i]
            odd += 2
            continue

        if odd >= len(arr):
            newarr[even] = arr[i]
            even += 2
            continue

        newarr[odd] = arr[i]
        odd += 2

    return newarr


arr = [1, -3, 5, 6, -3, 6, 7, -4, 9, 10]
newarr = rearrange(arr)
print(newarr)
