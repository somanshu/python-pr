# https://www.geeksforgeeks.org/maximum-difference-between-two-elements/


def cal_max_diff(arr):
    max_diff = 0
    small = 0

    for i in range(1, len(arr)):
        if arr[i] < arr[small]:
            small = i
            continue

        diff = arr[i] - arr[small]

        if diff > max_diff:
            max_diff = diff

    return max_diff


arr = [2, 3, 10, 6, 4, 8, 1]
arr = [7, 9, 5, 6, 3, 2]
res = cal_max_diff(arr)
print(res)
