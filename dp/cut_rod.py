# Cutting a Rod
# Given a rod of length n inches and an array of prices that contains prices of all
# pieces of size smaller than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces.


def get_max_price(length, price, mem):
    if length <= 0:
        return 0

    if mem[length - 1] > 0:
        return mem[length - 1]

    if length == 1:
        mem[0] = price[0]
        return price[0]

    if length == 2:
        res = max(price[1], 2 * price[0])
        mem[1] = res
        return mem[1]

    maxPrice = price[length - 1]

    left, right = 1, length - 1

    while left <= right:
        res = get_max_price(left, price, mem) + \
            get_max_price(right, price, mem)

        if res > maxPrice:
            maxPrice = res

        left += 1
        right -= 1

    mem[length - 1] = maxPrice
    return maxPrice


price = [1, 5, 8, 9, 10, 17, 17, 20]
length = len(price)
mem = [0 for i in range(length)]

print(get_max_price(length, price, mem))
