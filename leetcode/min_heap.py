class MinHeap:
    def __init__(self):
        self.heap = []

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify(self, i):
        small = i
        left = self.left_child(i)
        right = self.right_child(i)
        if left < len(self.heap) and self.heap[small] > self.heap[left]:
            small = left
        if right < len(self.heap) and self.heap[small] > self.heap[right]:
            small = right
        if small != i:
            self.swap(small, i)
            self.heapify(small)

    def push(self, key):
        self.heap.insert(0, key)
        self.heapify(0)

    def pop(self):
        if not self.heap:
            return
        key = self.heap[0]
        self.swap(0, len(self.heap) - 1)
        self.heap.pop()
        self.heapify(0)
        return key

    def peek(self):
        return self.heap[0] if self.heap else None


# 使用示例
min_heap = MinHeap()
min_heap.push(15)
min_heap.push(10)
min_heap.push(20)
min_heap.push(17)
min_heap.push(8)
min_heap.push(1)
min_heap.push(2)
min_heap.push(3)
min_heap.push(12)
print(min_heap.heap)

print(min_heap.pop())  # 输出 8
print(min_heap.heap)
print(min_heap.peek()) # 输出 10
