# https://www.geeksforgeeks.org/subarraysubstring-vs-subsequence-and-programs-to-generate-them/


def subsequence(ori_arr, arr, index):
    if index < 0:
        if not len(arr):
            return
        print(arr)
        return

    subsequence(ori_arr, arr, index - 1)
    arr.insert(0, ori_arr[index])
    subsequence(ori_arr, arr, index - 1)
    arr.pop(0)


def subarray(arr):
    count = 0

    for i in range(len(arr) + 1):
        for j in range(i):
            cur_arr = arr[j:i]

            if len(cur_arr):
                count += 1
                print(cur_arr)

    print(count)


arr = [1, 2, 3, 4]
subarray(arr)
subsequence(arr, [], len(arr) - 1)
