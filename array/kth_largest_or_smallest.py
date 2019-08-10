def maxHeapify(arr, index):
    left = 2 * index + 1
    right = 2 * index + 2

    val = arr[index]

    if left < len(arr) and val < arr[left]:
        val = arr[left]

    if right < len(arr) and val < arr[right]:
        val = arr[right]

    if left < len(arr) and val == arr[left]:
        arr[left], arr[index] = arr[index], arr[left]
    elif right < len(arr) and val == arr[right]:
        arr[right], arr[index] = arr[index], arr[right]

    return


def heapify(arr):
    n = len(arr)

    for i in range(n // 2, -1, -1):
        maxHeapify(arr, i)


def deleteMax(arr):
    tmp = arr[0]
    arr[0] = arr[-1]
    arr.pop(-1)

    maxHeapify(arr, 0)

    return tmp


def getKthLargest(arr, k):
    heapify(arr)

    for i in range(k):
        val = deleteMax(arr)

    return val


arr = [7, 10, 4, 3, 20, 15]
k = 4
res = getKthLargest(arr, k)

print(res)
