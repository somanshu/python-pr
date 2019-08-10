def bubblesort(numberList = []):
    n = len(numberList);
    for i in range(1, n):
        for j in range(i, 0, -1):
            if numberList[j] < numberList[j-1]:
                tmp = numberList[j];
                numberList[j] = numberList[j-1];
                numberList[j-1] = tmp;

def sort2(num = []):
	n = len(num);
	for i in range(0, n):
		for j in range(0, n-i-1):
			if num[j] > num[j+1]:
				tmp = num[j];
				num[j] = num[j+1];
				num[j+1] = tmp;

arr = [64, 34, 25, 12, 22, 11, 90];
bubblesort(arr);
# sort2(arr);
print(arr);
