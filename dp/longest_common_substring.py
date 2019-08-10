# https://www.geeksforgeeks.org/longest-common-substring-dp-29/


def lcs(i, j, str1, str2, count):
    if i == 0 or j == 0:
        return count

    if str1[i-1] == str2[j-1]:
        return lcs(i-1, j-1, str1, str2, count + 1)

    return max(count, lcs(i-1, j, str1, str2, 0), lcs(i, j-1, str1, str2, 0))


str1 = 'abcdxyz'
str2 = 'xyzabcd'
res = lcs(len(str1), len(str2), str1, str2, 0)
print(res)
