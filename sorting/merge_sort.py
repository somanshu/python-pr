import math

def merge_sort(num = []):
	if len(num) <= 1:
		return

	middle = len(num) // 2
	left_arr = num[:middle]
	right_arr = num[middle:]

	merge_sort(left_arr)
	merge_sort(right_arr)

	merge(left_arr, right_arr, num)

def merge(left_arr, right_arr, num):
	i = j = k = 0

	while i < len(left_arr) and j < len(right_arr):
			if left_arr[i] < right_arr[j]:
				num[k] = left_arr[i]
				i += 1
				k += 1
			else:
				num[k] = right_arr[j]
				j += 1
				k += 1

	while i < len(left_arr):
			num[k] = left_arr[i]
			i += 1
			k += 1

	while j < len(right_arr):
			num[k] = right_arr[j]
			j += 1
			k += 1


arr = [64, 34, 25, 12, 22, 11, 90];
merge_sort(arr)
print(arr)
