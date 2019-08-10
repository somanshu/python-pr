# Largest divisible pairs subset
# Input : arr[] = {10, 5, 3, 15, 20}
# Output : 3
# Explanation: The largest subset is 10, 5, 20.
# 10 is divisible by 5, and 20 is divisible by 10.


def get_largest(arr):
    n = len(arr)
    arr.sort()

    dp = [0 for i in range(n)]
    path = [f"{arr[i]}" for i in range(n)]
    dp[n-1] = 1

    for i in range(n-2, -1, -1):
        dp[i] = 1

        for j in range(i+1, n):
            if (arr[j] % arr[i] == 0):
                path[i] = f"{path[i]} {path[j]}"
                dp[i] += dp[j]
                break

    resIndex = dp.index(max(dp))
    return {
        "val": dp[resIndex],
        "path": path[resIndex]
    }


arr = [1, 3, 6, 13, 17, 18]
print(get_largest(arr))
