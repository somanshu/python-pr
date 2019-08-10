def sortInWave(arr):
    for i in range(len(arr)-1):
        if i % 2 == 0 and arr[i] <= arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        if i % 2 != 0 and arr[i] >= arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]


arr = [10, 90, 49, 2, 1, 5, 23]
sortInWave(arr)
print(arr)
