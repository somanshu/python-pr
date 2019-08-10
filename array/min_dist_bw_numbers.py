# https://www.geeksforgeeks.org/find-the-minimum-distance-between-two-numbers/


def cal_min_distance(arr, x, y):
    prev_index = None
    min_gap = len(arr)

    for i in range(len(arr)):
        if arr[i] == x or arr[i] == y:
            prev_index = i
            break

    for i in range(prev_index + 1, len(arr)):
        if (arr[prev_index] == x and arr[i] == y) or (arr[prev_index] == y and arr[i] == x):
            gap = i - prev_index
            if gap < min_gap:
                min_gap = gap

        if arr[i] == x or arr[i] == y:
            prev_index = i

    return min_gap


arr = [3, 5, 4, 2, 6, 3, 0, 0, 5, 4, 8, 3]
x = 3
y = 6
res = cal_min_distance(arr, x, y)
print(res)
