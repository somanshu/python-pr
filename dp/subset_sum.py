# Given a set of non-negative integers, and a value sum, determine if
# there is a subset of the given set with sum equal to given sum.


def subset_sum(s, m, n, path):
    if n == 0:
        return {
            "path": path,
            "val": 1
        }

    if n < 0:
        return None

    if m < 0:
        return None

    res1 = subset_sum(s, m-1, n, path)
    newPath = path[:]
    newPath.append(s[m])
    res2 = subset_sum(s, m-1, n-s[m], newPath)

    if res1 == None and res2 == None:
        return None

    if res1 == None:
        return res2

    if res2 == None:
        return res1

    path1 = res1["path"]
    path2 = res2["path"]
    allPaths = []
    allPaths.append(path1)
    allPaths.append(path2)

    return {
        "path": allPaths,
        "val": res1["val"] + res2["val"]
    }


s = [3, 34, 4, 12, 5, 2]
n = 9
m = len(s) - 1
print(subset_sum(s, m, n, []))
