# https: // www.geeksforgeeks.org/rearrange-array-arri/


def position_item(arr, item, index):
    if item == -1:
        return
    if arr[item] == item:
        return
    if arr[item] == -1:
        arr[item] = item
        arr[index] = -1
        return
    tmp = arr[item]
    arr[item] = item
    position_item(arr, tmp, item)


def rearrange(arr):
    for i in range(len(arr)):
        position_item(arr, arr[i], i)


def swap(arr):
    i = 0
    while i < len(arr):
        if arr[i] > 0 and arr[i] != i:
            tmp = arr[arr[i]]
            arr[arr[i]] = arr[i]
            arr[i] = tmp
        else:
            i += 1


arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
# rearrange(arr)
swap(arr)
print(arr)
