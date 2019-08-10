# Given a set of non-negative distinct integers, and a value m, determine if
# there is a subset of the given set with sum divisible by m.


def get_subset(s, index, m, currentSum):
    if currentSum > 0 and currentSum % m == 0:
        return True

    if index < 0:
        return False

    return get_subset(s, index - 1, m, currentSum) or get_subset(s, index - 1, m, currentSum + s[index])


s = [3, 1, 7, 5]
# s = [1, 6]
m = 6
# m = 5
index = len(s) - 1
print(get_subset(s, index, m, 0))
