import unittest
from heap import MinHeap


class TestMinHeap(unittest.TestCase):

    def test_insert_and_extract_min(self):
        heap = MinHeap()
        heap.insert(5)
        heap.insert(3)
        heap.insert(10)
        heap.insert(1)
        heap.insert(8)

        self.assertEqual(heap.extract_min(), 1)
        self.assertEqual(heap.extract_min(), 3)
        self.assertEqual(heap.extract_min(), 5)
        self.assertEqual(heap.extract_min(), 8)
        self.assertEqual(heap.extract_min(), 10)

    def test_insert_duplicates(self):
        heap = MinHeap()
        heap.insert(5)
        heap.insert(3)
        heap.insert(5)
        heap.insert(1)
        heap.insert(8)

        self.assertEqual(heap.extract_min(), 1)
        self.assertEqual(heap.extract_min(), 3)
        self.assertEqual(heap.extract_min(), 5)
        self.assertEqual(heap.extract_min(), 5)
        self.assertEqual(heap.extract_min(), 8)

    def test_get_min(self):
        heap = MinHeap()
        heap.insert(5)
        heap.insert(3)
        heap.insert(10)
        self.assertEqual(heap.get_min(), 3)
        heap.insert(1)
        self.assertEqual(heap.get_min(), 1)

    def test_is_empty(self):
        heap = MinHeap()
        self.assertTrue(heap.is_empty())
        heap.insert(5)
        self.assertFalse(heap.is_empty())
        heap.extract_min()
        self.assertTrue(heap.is_empty())

    def test_size(self):
        heap = MinHeap()
        self.assertEqual(heap.size(), 0)
        heap.insert(5)
        self.assertEqual(heap.size(), 1)
        heap.insert(3)
        self.assertEqual(heap.size(), 2)
        heap.extract_min()
        self.assertEqual(heap.size(), 1)

    def test_extract_min_empty(self):
        heap = MinHeap()
        with self.assertRaises(IndexError) as context:
            heap.extract_min()
        self.assertEqual(str(context.exception), "Cannot extract minimum: heap is empty")

    def test_get_min_empty(self):
        heap = MinHeap()
        with self.assertRaises(IndexError) as context:
            heap.get_min()
        self.assertEqual(str(context.exception), "Cannot get minimum: heap is empty")

    def test_insert_string(self):
        heap = MinHeap()
        with self.assertRaises(TypeError) as context:
            heap.insert("abc")
        self.assertEqual(str(context.exception), "Only numbers can be added to the heap")

    def test_insert_none(self):
        heap = MinHeap()
        with self.assertRaises(TypeError) as context:
            heap.insert(None)
        self.assertEqual(str(context.exception), "Only numbers can be added to the heap")

    def test_large_input(self):
        heap = MinHeap()
        for i in range(1000):
            heap.insert(i)

        for i in range(1000):
            self.assertEqual(heap.extract_min(), i)

    def test_random_input(self):
        import random
        heap = MinHeap()
        numbers = [random.randint(1, 1000) for _ in range(500)]
        for num in numbers:
            heap.insert(num)

        sorted_numbers = sorted(numbers)
        for num in sorted_numbers:
            self.assertEqual(heap.extract_min(), num)


if __name__ == '__main__':
    unittest.main()
