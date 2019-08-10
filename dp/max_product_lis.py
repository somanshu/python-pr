# https://www.geeksforgeeks.org/maximum-product-increasing-subsequence/


def max_product_lis(arr):
    l = arr[:]
    resArr = [[] for i in range(len(arr))]

    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j] and l[i] < l[j] * arr[i]:
                l[i] = l[j] * arr[i]
                resArr[i] = resArr[j][:]

        resArr[i].append(arr[i])

    maxProduct = 0
    index = 0
    for i in range(len(l)):
        if l[i] > maxProduct:
            maxProduct = l[i]
            index = i

    return (maxProduct, resArr[index])


arr = [3, 100, 4, 5, 150, 6]
res = max_product_lis(arr)
print(res)
