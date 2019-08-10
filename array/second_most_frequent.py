def getCharCountMap(string):
    charCountMap = {
    }
    for char in string:
        if char in charCountMap:
            charCountMap[char] += 1
        else:
            charCountMap[char] = 1
    return charCountMap


def second_most_frequent(string):
    charCountMap = getCharCountMap(string)
    first = string[0]
    second = string[0]

    for i in charCountMap:
        if charCountMap[i] > charCountMap[first]:
            second = first
            first = i
            continue
        if charCountMap[i] > charCountMap[second]:
            second = i
            continue
    return [first, second]


string = "geeksqukizk"
result = second_most_frequent(string)
print('most frequent --->', result[0])
print('second --->', result[1])
