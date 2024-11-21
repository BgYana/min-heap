class MinHeap:
    def __init__(self):
        self._heap = []

    def _parent(self, i):
        return (i - 1) // 2

    def _left_child(self, i):
        return 2 * i + 1

    def _right_child(self, i):
        return 2 * i + 2

    def _heapify_up(self, i):
        while i > 0 and self._heap[i] < self._heap[self._parent(i)]:
            self._heap[i], self._heap[self._parent(i)] = self._heap[self._parent(i)], self._heap[i]
            i = self._parent(i)

    def _heapify_down(self, i):
        while True:
            smallest = i
            left = self._left_child(i)
            right = self._right_child(i)

            if left < len(self._heap) and self._heap[left] < self._heap[smallest]:
                smallest = left
            if right < len(self._heap) and self._heap[right] < self._heap[smallest]:
                smallest = right

            if smallest == i:
                break

            self._heap[i], self._heap[smallest] = self._heap[smallest], self._heap[i]
            i = smallest

    def insert(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Only numbers can be added to the heap")
        self._heap.append(value)
        self._heapify_up(len(self._heap) - 1)

    def extract_min(self):
        if not self._heap:
            raise IndexError("Cannot extract minimum: heap is empty")
        min_value = self._heap[0]
        self._heap[0] = self._heap.pop()
        self._heapify_down(0)
        return min_value

    def get_min(self):
        if not self._heap:
            raise IndexError("Cannot get minimum: heap is empty")
        return self._heap[0]

    def is_empty(self):
        return not self._heap

    def size(self):
        return len(self._heap)
    
