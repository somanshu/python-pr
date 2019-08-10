# https://www.geeksforgeeks.org/find-subarray-least-average/


def leastAvg(arr, k):
    summation = []
    summation.append(0)
    summation.append(arr[0])
    min_avg = 9999
    min_avg_last_index = None

    for i in range(2, len(arr) + 1):
        summation.append(summation[i-1] + arr[i-1])

    for i in range(3, len(arr) + 1):
        cur_sum = summation[i] - summation[i-k]
        avg_sum = cur_sum // k

        if avg_sum < min_avg:
            min_avg = avg_sum
            min_avg_last_index = i - 1

    return (min_avg, min_avg_last_index - k + 1, min_avg_last_index)


arr = [3, 7, 90, 20, 10, 50, 40]
arr = [3, 7, 5, 20, -10, 0, 12]
k = 2
res = leastAvg(arr, k)
print(res)
