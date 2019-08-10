import functools


def compareConcat(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)

    if int(ab) > int(ba):
        return -1

    if int(ab) < int(ba):
        return 1

    return 0


def largestConcat(arr):
    res = sorted(arr, key=functools.cmp_to_key(compareConcat))
    res = map(lambda x: str(x), res)
    return "".join(res)


arr = [1, 34, 3, 98, 9, 76, 45, 4]
res = largestConcat(arr)
print(res)
