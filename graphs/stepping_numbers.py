# Stepping Numbers
# https://www.geeksforgeeks.org/stepping-numbers/


def bfs_approach(totalDigits, y, x, i, sol):
    queue = []
    queue.append((i, str(i)))

    while len(queue) > 0:
        (d, num) = queue.pop(0)
        if int(num) >= x and int(num) <= y:
            sol.append(int(num))
        if d > 0 and len(num) < totalDigits and int(num+str(d-1)) <= y and int(num+str(d-1)) >= x:
            queue.append((d-1, num+str(d-1)))
        if d < 9 and len(num) < totalDigits and int(num+str(d+1)) <= y and int(num+str(d+1)) >= x:
            queue.append((d+1, num+str(d+1)))


def getSteppingNumberByBfs(x, y):
    totalDigits = len(str(y))
    sol = []
    if x == 0:
        sol.append(0)
    for i in range(1, 10):
        bfs_approach(totalDigits, y, x, i, sol)

    sol.sort()
    print(sol)


def dfs_approach(i, x, y, sol):
    number = int(i)
    lastDigit = int(i[-1:])

    if number > y or number < x:
        return

    sol.append(number)

    if lastDigit < 9:
        dfs_approach(i + str(lastDigit + 1), x, y, sol)

    if lastDigit > 0:
        dfs_approach(i + str(lastDigit - 1), x, y, sol)


def getSteppingNumberByDfs(x, y):
    totalDigits = len(str(y))
    sol = []
    if x == 0:
        sol.append(0)

    for i in range(1, 10):
        dfs_approach(str(i), x, y, sol)

    sol.sort()
    print(sol)


getSteppingNumberByBfs(0, 121)
getSteppingNumberByDfs(0, 121)
