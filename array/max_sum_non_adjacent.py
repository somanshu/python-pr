# https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/


def max_sum_disjoint_1(arr):
    dp = [arr[i] for i in range(len(arr))]

    for i in range(len(arr)):
        for j in range(0, i-1):
            if dp[i] < dp[j] + arr[i]:
                dp[i] = dp[j] + arr[i]

    return dp


def max_sum_disjoint(arr):
    dp = [None for i in range(len(arr))]
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for i in range(2, len(arr)):
        dp[i] = max(arr[i] + dp[i-2], dp[i-1])

    return dp


arr = [5, 5, 10, 100, 10, 5]
# arr = [1, 2, 3]
# arr = [1, 20, 3]
res = max_sum_disjoint(arr)
print(res)
