# https://www.geeksforgeeks.org/maximum-profit-by-buying-and-selling-a-share-at-most-twice/


def cal_max_profit(arr):
    n = len(arr)
    profit = [0] * n
    max_price = arr[-1]

    for i in range(n-2, -1, -1):
        if arr[i] > max_price:
            max_price = arr[i]

        profit[i] = max(profit[i+1], max_price - arr[i])

    min_price = arr[0]
    for i in range(1, n):
        if arr[i] < min_price:
            min_price = arr[i]

        profit[i] = max(profit[i-1], profit[i] + arr[i] - min_price)

    return profit[n-1]


arr = [2, 30, 15, 10, 8, 25, 80]
res = cal_max_profit(arr)
print(res)
