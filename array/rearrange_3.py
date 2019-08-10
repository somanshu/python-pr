# https://www.geeksforgeeks.org/rearrange-array-arrj-becomes-arri-j/


def rearrange(arr):
    newarr = [None for i in range(len(arr))]
    for i in range(len(arr)):
        newarr[arr[i]] = i

    return newarr


arr = [2, 0, 1, 4, 5, 3]
res = rearrange(arr)
print(res)
