# https://www.geeksforgeeks.org/reorder-a-array-according-to-given-indexes/


def rearrange(arr, ind):
    newarr = [0] * len(arr)

    for i in range(len(ind)):
        newarr[ind[i]] = arr[i]

    return newarr


arr = [50, 40, 70, 60, 90]
ind = [3, 0, 4, 1, 2]
res = rearrange(arr, ind)
print(res)
