def together(arr, k):
    count = 0
    swaps = 0

    for i in range(len(arr)):
        if arr[i] <= k:
            arr[i], arr[count] = arr[count], arr[i]
            if i != count:
                swaps += 1
            count += 1

    return swaps


arr = [2, 7, 9, 5, 8, 7, 4]
k = 5
swaps = together(arr, k)
print(arr, swaps)
