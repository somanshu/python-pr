# nlogn complexity


def isSmallest(val, activeLists):
    for ls in activeLists:
        if ls[0] < val:
            return False

    return True


def isLargest(val, activeLists):
    for ls in activeLists:
        if ls[-1] > val:
            return False

    return True


def getBiggestList(activeLists):
    maxLength = 0
    biggest = []
    for ls in activeLists:
        if len(ls) > maxLength:
            maxLength = len(ls)
            biggest = ls

    return biggest


def getList(activeLists, val):
    maxLength = 0
    index = 0

    for i in range(len(activeLists)):
        if activeLists[i][-1] <= val and len(activeLists[i]) > maxLength:
            maxLength = len(activeLists[i])
            index = i

    return activeLists[index]


def discardLists(activeLists, length):
    updatedLists = list(filter(lambda ls: len(ls) != length, activeLists))
    return updatedLists


def lis(arr):
    activeLists = []

    for i in range(len(arr)):
        if (isSmallest(arr[i], activeLists)):
            activeLists.append([arr[i]])
            continue

        if isLargest(arr[i], activeLists):
            newlist = getBiggestList(activeLists)[:]
            newlist.append(arr[i])
            activeLists.append(newlist)
            continue

        newlist = getList(activeLists, arr[i])[:]
        newlist.append(arr[i])
        activeLists = discardLists(activeLists, len(newlist))
        activeLists.append(newlist)

    return getBiggestList(activeLists)


arr = [2, 5, 3, 7, 11, 8, 10, 13, 6]
res = lis(arr)
print(res)
