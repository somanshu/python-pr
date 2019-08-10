# https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/


def largestSum(arr):
    curr_sum = arr[0]
    sol = arr[0]

    for i in range(1, len(arr)):
        curr_sum += arr[i]

        if curr_sum < 0:
            curr_sum = 0
            continue

        if curr_sum > sol:
            sol = curr_sum

    return sol


arr = [-2, -3, 4, -1, -2, 1, 5, -3]
res = largestSum(arr)
print(res)
