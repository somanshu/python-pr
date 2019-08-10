# https://www.geeksforgeeks.org/k-th-largest-sum-contiguous-subarray/


class Heap():
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.bottomUpHeapify(len(self.heap) - 1)

    def bottomUpHeapify(self, index):
        parent = index // 2

        while self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = index // 2

    def getMin(self):
        return self.heap[0]

    def minHeapify(self, index):
        left = 2 * index + 1
        right = 2 * index + 2

        minIndex = index

        if left < len(self.heap) and self.heap[left] < self.heap[minIndex]:
            minIndex = left

        if right < len(self.heap) and self.heap[right] < self.heap[minIndex]:
            minIndex = right

        if minIndex != index:
            self.heap[index], self.heap[minIndex] = self.heap[minIndex], self.heap[index]
            self.minHeapify(minIndex)

    def replaceMin(self, val):
        self.heap[0] = val
        self.minHeapify(0)


def sum_contiguos(arr, k):
    heap = Heap()

    summation = []
    summation.append(0)
    summation.append(arr[0])

    for i in range(2, len(arr) + 1):
        summation.append(summation[i-1] + arr[i-1])

    for i in range(1, len(arr) + 1):
        for j in range(i, len(arr) + 1):
            x = summation[j] - summation[i-1]

            if len(heap.heap) < k:
                heap.insert(x)
            elif heap.getMin() < x:
                heap.replaceMin(x)

    return heap.getMin()


def sum_recursive_util(arr, index, k, net_sum, res, hashmap):
    if index == len(arr):
        return

    if len(res.heap) < k and net_sum not in hashmap:
        res.insert(net_sum)
        hashmap[net_sum] = True
    elif res.getMin() < net_sum and net_sum not in hashmap:
        res.replaceMin(net_sum)
        hashmap[net_sum] = True

    sum_recursive_util(arr, index + 1, k, net_sum + arr[index], res, hashmap)
    sum_recursive_util(arr, index + 1, k, arr[index], res, hashmap)


def sum_recursive(arr, k):
    res = Heap()
    sum_recursive_util(arr, 0, k, 0, res, {})
    return res.getMin()


arr = [4, -8, 9, -4, 1, -8, -1, 6]
k = 4
res = sum_contiguos(arr, k)
print(res)
