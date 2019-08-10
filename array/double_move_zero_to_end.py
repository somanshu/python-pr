# https://www.geeksforgeeks.org/double-first-element-move-zero-end/


def rearrange(arr):
    newarr = []

    for i in range(len(arr)):
        if arr[i] == 0:
            continue

        if i < len(arr) - 1 and arr[i+1] == arr[i]:
            arr[i] = 2 * arr[i]
            arr[i+1] = 0
            newarr.append(arr[i])
            continue

        newarr.append(arr[i])

    zeros = len(arr) - len(newarr)

    for i in range(zeros):
        newarr.append(0)

    return newarr


arr = [0, 2, 2, 2, 0, 6, 6, 0, 0, 8]
res = rearrange(arr)
print(res)
