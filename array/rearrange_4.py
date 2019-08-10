# https://www.geeksforgeeks.org/rearrange-array-even-index-elements-smaller-odd-index-elements-greater/


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def rearrange(arr):
    for i in range(len(arr) - 1):
        if i % 2 == 0 and arr[i] > arr[i+1]:
            swap(arr, i, i+1)
            continue
        if i % 2 != 0 and arr[i] < arr[i+1]:
            swap(arr, i, i+1)


arr = [6, 4, 2, 1, 8, 3]
rearrange(arr)
print(arr)
