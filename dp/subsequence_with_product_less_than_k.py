# Count all subsequences having product less than K
# https://www.geeksforgeeks.org/count-subsequences-product-less-k/


def getCount(index, product, arr, k):
    if index == 0 and product == None:
        if arr[index] <= k:
            return 1
        return 0

    if index == 0:
        if arr[index] * product <= k:
            # { arr[index] } and { arr[index], items that make the product }
            return 2
        # { items that make the product }
        return 1

    count = 0
    # don't include arr[index] in the result counts
    count += getCount(index - 1, product, arr, k)

    # include arr[index] in the result counts
    if product == None and arr[index] <= k:
        count += getCount(index - 1, arr[index], arr, k)
    elif product and product * arr[index] <= k:
        count += getCount(index - 1, product * arr[index], arr, k)

    return count


arr = [1, 2, 3, 4, 5]
k = 10
res = getCount(len(arr) - 1, None, arr, k)
print(res)
