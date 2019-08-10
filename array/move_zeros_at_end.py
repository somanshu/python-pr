# https://www.geeksforgeeks.org/move-zeroes-end-array/


def moveToEnd(arr):
    end = len(arr) - 1

    for i in range(len(arr)):
        if arr[i] != 0:
            continue

        while arr[end] == 0:
            end -= 1

        if end <= i:
            break

        tmp = arr[i]
        arr[i] = arr[end]
        arr[end] = tmp


def moveToEnd2(arr):
    count = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count += 1


arr = [1, 2, 0, 0, 0, 3, 6]
moveToEnd2(arr)
print(arr)
