def max_profit(arr):
    small = 0
    sol = []

    for i in range(1, len(arr)):
        if arr[small] > arr[i]:
            small = i
            continue

        profit = arr[i] - arr[small]

        # when sol is empty and we have some profit then just append
        if not len(sol):
            sol.append((small, i, profit))
            continue

        (prevSmall, prevIndex, prevProfit) = sol[-1]

        # here update only if more profit and overwrite result
        if small == prevSmall:
            if prevProfit < profit:
                sol[-1] = (small, i, profit)
            continue

        # if new small then just append
        sol.append((small, i, profit))

    return sol


arr = [100, 180, 260, 310, 40, 50, 60]
# arr = [9, 7, 8, 12, 5, 4, 10]
res = max_profit(arr)
print(res)
