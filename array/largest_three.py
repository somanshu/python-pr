def getThreeLargest(arr):
    first = arr[0]
    second = -1
    third = -1

    for i in range(1, len(arr)):
        if arr[i] > first:
            third = second
            second = first
            first = arr[i]

        elif arr[i] > second:
            third = second
            second = arr[i]

        elif arr[i] > third:
            third = arr[i]

    return (first, second, third)


arr = [10, 4, 3, 50, 23, 90]
res = getThreeLargest(arr)
print(res)
