# https://www.geeksforgeeks.org/rearrange-array-such-that-even-positioned-are-greater-than-odd/


def rearrange(arr):
    arr.sort()

    index = 0

    newarr = arr[:]

    for i in range(len(arr)):
        newarr[index] = arr[i]
        index += 2

        if index > len(arr):
            index = 1

    return newarr


arr = [1, 3, 2, 2, 5]
res = rearrange(arr)
print(res)
