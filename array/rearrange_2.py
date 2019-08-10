# https://www.geeksforgeeks.org/rearrange-array-order-smallest-largest-2nd-smallest-2nd-largest/


def rearrange(arr):
    arr.sort()
    newarr = []
    start = 0
    end = len(arr) - 1

    while start < end:
        newarr.append(arr[start])
        newarr.append(arr[end])
        start += 1
        end -= 1

    if start == end:
        newarr.append(arr[start])

    return newarr


arr = [5, 8, 1, 4, 2, 9, 3, 7, 6]
res = rearrange(arr)
print(res)
