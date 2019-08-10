def doesSubsetExist(arr, sumTotal):
    hashmap = {}
    hashmap[arr[0]] = True

    if arr[0] == sumTotal:
        return True

    for i in range(1, len(arr)):
        if arr[i] == sumTotal:
            return True

        vals = list(hashmap.keys())
        for val in vals:
            if val + arr[i] not in hashmap:
                hashmap[val + arr[i]] = True
                if val + arr[i] == sumTotal:
                    return True

            if arr[i] not in hashmap:
                hashmap[arr[i]] = True

    return False


arr = [1, 1, 2, 3, 4]
sumTotal = 6
res = doesSubsetExist(arr, sumTotal)
print(res)
