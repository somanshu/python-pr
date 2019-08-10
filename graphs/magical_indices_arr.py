# https://www.geeksforgeeks.org/magical-indices-array/


def mark_indices(index, magical, arr):
    if magical[index]:
        return

    magical[index] = True
    mark_indices((index + arr[index] + 1) % len(arr), magical, arr)


def findIndices(arr):
    n = len(arr)
    magical = [False for i in range(n)]
    visited = [False for i in range(n)]
    parent = [None for i in range(n)]

    for i in range(n):
        if parent[i] == None:
            j = i
            while parent[j] == None:
                parent[j] = i
                j = (j + arr[j] + 1) % n

            if parent[j] == i:
                mark_indices(j, magical, arr)

    for i in range(len(magical)):
        if magical[i]:
            print(i)


arr = [1, 1, 1, 1]
# arr = [0, 0, 0, 2]
findIndices(arr)
