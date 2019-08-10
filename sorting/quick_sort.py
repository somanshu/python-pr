def swap(arr, i, j):
	tmp = arr[i]
	arr[i] = arr[j]
	arr[j] = tmp

def partition(num, left, right):
	pivot = num[right]
	low_index = left - 1

	for i in range(left, right):
		if num[i] <= pivot:
			low_index += 1
			swap(num, i, low_index)

	swap(num, low_index+1, right)
	return low_index + 1;



def quick_sort(num, left, right):
	if left >= right:
		return

	pi = partition(num, left, right)
	quick_sort(num, left, pi - 1)
	quick_sort(num, pi + 1, right)

arr = [64, 34, 25, 12, 22, 11, 90];
quick_sort(arr, 0, len(arr) - 1)
print(arr)
