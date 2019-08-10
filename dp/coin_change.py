# Given a value N, if we want to make change for N cents, and we have infinite
# supply of each of S = {S1, S2, .., Sm} valued coins, how many ways can we make the change?
# The order of coins doesn’t matter.
# For example, for N = 4 and S = {1, 2, 3}, there are four solutions:
# {1, 1, 1, 1}, {1, 1, 2}, {2, 2}, {1, 3}. So output should be 4. For N = 10 and S = {2, 5, 3, 6},
# there are five solutions: {2, 2, 2, 2, 2}, {2, 2, 3, 3}, {2, 2, 6}, {2, 3, 5} and {5, 5}. So the output should be 5.

# s = []
# m is the index if s
# n is the value which needs to be changed into coins


def coin_change(s, m, n):
    if n == 0:
        return 1

    if n < 0:
        return 0

    if m < 0:
        return 0

    return coin_change(s, m-1, n) + coin_change(s, m, n-s[m])


# s = [2, 5, 3, 6]
s = [1, 2, 3]
# n = 10
n = 4
m = len(s) - 1
print(coin_change(s, m, n))
