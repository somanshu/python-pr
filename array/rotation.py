# method 1
def rotateBySpace(num, rotations):
    if rotations > len(num):
        rotations = rotations - len(num)

    tmp = num[:rotations]

    for i in range(len(num) - rotations):
        num[i] = num[i+rotations]

    num[rotations:] = tmp[:]

# method 2


def rotationByOne(num=[]):
    tmp = num[0]
    for i in range(len(num) - 1):
        num[i] = num[i+1]

    num[len(num) - 1] = tmp


def rotationByN(num, rotations):
    for i in range(rotations):
        rotationByOne(num)

# method 3


def rotate(num, start, end):
    while start < end:
        tmp = num[start]
        num[start] = num[end - 1]
        num[end - 1] = tmp
        start += 1
        end -= 1


def rotationReverse(num, rotations):
    rotate(num, 0, rotations)
    rotate(num, rotations, len(num))
    rotate(num, 0, len(num))


def swap(arr, fi, si, d):
    for i in range(d):
        temp = arr[fi + i]
        arr[fi + i] = arr[si + i]
        arr[si + i] = temp


def leftRotate(arr, d, n):
    if(d == 0 or d == n):
        return
    i = d
    j = n - d
    while (i != j):

        if(i < j):  # A is shorter
            swap(arr, d - i, d + j - i, i)
            j -= i

        else:  # B is shorter
            swap(arr, d - i, d, j)
            i -= j

    swap(arr, d - i, d, i)


def blockSwap(arr, d):
    n = len(arr)
    sizeOfA = d
    sizeOfB = n-d
    startA = 0
    startB = d

    if (d == 0 or d == n):
        return

    while sizeOfA != sizeOfB:
        if sizeOfA < sizeOfB:
            posB = startB + sizeOfB - sizeOfA
            swap(arr, startA, posB, sizeOfA)
            sizeOfB = sizeOfB - sizeOfA
        else:
            swap(arr, startA, startB, sizeOfB)
            sizeOfA = sizeOfA - sizeOfB
            startA = startA + sizeOfB

    swap(arr, startA, startB, sizeOfA)


# arr = [64, 34, 25, 12, 22, 11, 90]
# rotateBySpace(arr, 3)
# rotationByN(arr, 5)
# rotationReverse(arr, 5)
arr = [1, 2, 3, 4, 5, 6, 7]
# leftRotate(arr, 4, 7)
blockSwap(arr, 5)
print(arr)
