# https://www.geeksforgeeks.org/k-maximum-sum-overlapping-contiguous-sub-arrays/


class Heap():
    def __init__(self):
        self.heap = []

    def bottomUpHeapify(self, index):
        parent = index // 2

        while self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = index // 2

    def insert(self, val):
        self.heap.append(val)
        self.bottomUpHeapify(len(self.heap) - 1)

    def delete(self):
        val = self.heap.pop(-1)

        if len(self.heap) > 0:
            self.heap[0] = val
            self.minHeapify(0)

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


def k_max_sum_contiguos(arr, k):
    summation = []
    summation.append(0)
    summation.append(arr[0])
    h = Heap()

    for i in range(2, len(arr) + 1):
        summation.append(arr[i-1] + summation[i-1])

    for i in range(1, len(arr) + 1):
        for j in range(i, len(arr) + 1):
            x = summation[j] - summation[i-1]

            if len(h.heap) < k:
                h.insert(x)
            elif h.getMin() < x:
                h.replaceMin(x)

    res = []
    for i in range(k):
        res.append(h.getMin())
        h.delete()

    res.reverse()
    return res


arr = [-2, -3, 4, -1, -2, 1, 5, -3]
k = 3
res = k_max_sum_contiguos(arr, k)
print(res)
