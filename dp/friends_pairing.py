# Input  : n = 3
# Output : 4

# Explanation
# {1}, {2}, {3} : all single
# {1}, {2, 3} : 2 and 3 paired but 1 is single.
# {1, 2}, {3} : 1 and 2 are paired but 3 is single.
# {1, 3}, {2} : 1 and 3 are paired but 2 is single.
# Note that {1, 2} and {2, 1} are considered same.


def pairs(n):
    if n <= 2:
        return n
    return pairs(n-1) + (n-1) * pairs(n-2)


print(pairs(4))
