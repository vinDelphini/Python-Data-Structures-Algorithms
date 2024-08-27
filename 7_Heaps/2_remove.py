class MaxHeap:

    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return (index * 2) + 1

    def _right_child(self, index):
        return (index * 2) + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1

        while index > 0 and self.heap[index] > self.heap[self._parent(index)]:
            self._swap(index1=index, index2=self._parent(index))
            index = self._parent(index)

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

myheap = MaxHeap()
myheap.insert(61)
myheap.insert(99)
myheap.insert(72)

myheap.insert(58)

print(myheap.heap)

myheap.insert(100)

print(myheap.heap)

myheap.insert(75)

print(myheap.heap)

"""
    EXPECTED OUTPUT:
    ----------------
    [99, 72, 61, 58]
    [100, 99, 61, 58, 72]
    [100, 99, 75, 58, 72, 61]

"""
