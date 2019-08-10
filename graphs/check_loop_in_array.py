# Check loop in array according to given constraints
# https://www.geeksforgeeks.org/check-loop-array-according-given-constraints/


def check_cycle(index, arr, visited, recStack):
    visited[index] = True
    recStack[index] = True

    if arr[index] != 0:
        newIndex = (index + arr[index]) % len(arr)
        if newIndex != index and recStack[newIndex]:
            return True

        if not visited[newIndex]:
            if check_cycle(newIndex, arr, visited, recStack):
                return True

    recStack[index] = False
    return False


def detectLoop(arr):
    visited = [False for i in range(len(arr))]
    recStack = [False for i in range(len(arr))]

    for i in range(len(arr)):
        if not visited[i]:
            if check_cycle(i, arr, visited, recStack):
                return True

    return False


arr = [2, -1, 1, 2, 2]
# arr = [1, 1, 1, 1, 1, 1]
# arr = [1, 2]
res = detectLoop(arr)
print(res)
