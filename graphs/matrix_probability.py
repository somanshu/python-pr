# A matrix probability question
# https://www.geeksforgeeks.org/a-matrix-probability-question/


def isSafe(x, y, n):
    return x >= 0 and y >= 0 and x < n and y < n


def findProbability(steps, x, y, size):
    if not isSafe(x, y, size):
        return 0

    if steps == 0:
        return 1

    prob = 0

    prob += findProbability(steps-1, x-1, y, size) * 0.25
    prob += findProbability(steps-1, x+1, y, size) * 0.25
    prob += findProbability(steps-1, x, y-1, size) * 0.25
    prob += findProbability(steps-1, x, y+1, size) * 0.25

    return prob


def getCount(steps, x, y, size):
    if not isSafe(x, y, size):
        return 0

    if steps == 0:
        return 1

    return getCount(steps - 1, x-1, y, size) + getCount(steps - 1, x+1, y, size) + getCount(steps - 1, x, y+1, size) + getCount(steps - 1, x, y-1, size)


def findProb(steps, x, y, size):
    count = getCount(steps, x, y, size)
    return count / (4**steps)


res = findProbability(2, 1, 1, 5)
print(res)
res = findProb(2, 1, 1, 5)
print(res)
