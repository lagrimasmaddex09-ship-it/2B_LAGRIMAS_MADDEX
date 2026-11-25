import random


class MinHeap:
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def extract(self):
        if not self.heap:
            return None
        smallest = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._sift_down(0)
        return smallest

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[parent] <= self.heap[i]:
                break
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent

    def _sift_down(self, i):
        n = len(self.heap)
        while True:
            best = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and self.heap[left] < self.heap[best]:
                best = left
            if right < n and self.heap[right] < self.heap[best]:
                best = right

            if best == i:
                break

            self.heap[i], self.heap[best] = self.heap[best], self.heap[i]
            i = best

# Activity 2: Max-heap
class MaxHeap:
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def extract(self):
        if not self.heap:
            return None
        largest = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._sift_down(0)
        return largest

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[parent] >= self.heap[i]:
                break
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent

    def _sift_down(self, i):
        n = len(self.heap)
        while True:
            best = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and self.heap[left] > self.heap[best]:
                best = left
            if right < n and self.heap[right] > self.heap[best]:
                best = right

            if best == i:
                break

            self.heap[i], self.heap[best] = self.heap[best], self.heap[i]
            i = best


# Activity 3: Heap sort using max-heap
def heap_sort(arr):
    h = MaxHeap()
    for num in arr:
        h.insert(num)

    result = []
    while h.size() > 0:
        result.append(h.extract())

    result.reverse()
    return result


# Activity 4: Kth largest using a min-heap of size k
def kth_largest(nums, k):
    if not nums or k <= 0 or k > len(nums):
        return None

    h = MinHeap()
    for num in nums:
        if h.size() < k:
            h.insert(num)
        elif num > h.peek():
            h.extract()
            h.insert(num)

    return h.peek()


# Activity 5: Merge k sorted arrays using min-heap of (value, array_index, element_index)
def merge_k_arrays(arrays):
    h = MinHeap()
    merged = []

    for arr_idx, arr in enumerate(arrays):
        if arr:
            h.insert((arr[0], arr_idx, 0))

    while h.size() > 0:
        val, arr_idx, elem_idx = h.extract()
        merged.append(val)

        next_idx = elem_idx + 1
        if next_idx < len(arrays[arr_idx]):
            h.insert((arrays[arr_idx][next_idx], arr_idx, next_idx))

    return merged


# Activity 6: Priority scheduler (stretch)
class PriorityScheduler:
    def __init__(self):
        self.pq = MaxHeap()
        self.seq = 0

    def add_job(self, job, priority):
        self.pq.insert((priority, -self.seq, job))
        self.seq += 1

    def run_scheduler(self):
        released = []
        while self.pq.size() > 0:
            priority, _, job = self.pq.extract()
            released.append((job, priority))
        return released


if __name__ == "__main__":
    # Activity 1 test
    min_h = MinHeap()
    for x in [5, 9, 11, 14, 19, 17, 18, 13]:
        min_h.insert(x)
    act1_out = [min_h.extract() for _ in range(min_h.size())]
    print("Activity 1 (Min-Heap extract):", act1_out)

    # Activity 2 test
    max_h = MaxHeap()
    for x in [5, 9, 11, 14, 19, 17, 18, 13]:
        max_h.insert(x)
    act2_out = [max_h.extract() for _ in range(max_h.size())]
    print("Activity 2 (Max-Heap extract):", act2_out)

    # Activity 3 test
    print("Activity 3 [4, 10, 3, 5, 1]:", heap_sort([4, 10, 3, 5, 1]))
    print("Activity 3 sorted:", heap_sort([1, 2, 3, 4, 5]))
    print("Activity 3 reverse:", heap_sort([5, 4, 3, 2, 1]))
    print("Activity 3 duplicates:", heap_sort([3, 1, 2, 3, 1]))
    print("Activity 3 empty:", heap_sort([]))

    # Activity 4 test
    nums = [7, 2, 9, 4, 15, 6]
    k = 3
    print("Activity 4 kth largest:", kth_largest(nums, k), "| check:", sorted(nums, reverse=True)[k - 1])

    # Activity 5 test
    a = [1, 5, 9]
    b = [2, 6, 10, 14]
    c = [0, 3]
    print("Activity 5 merged:", merge_k_arrays([a, b, c]))

    # Activity 6 test
    sched = PriorityScheduler()
    sched.add_job("Email check", 2)
    sched.add_job("Crash fix", 10)
    sched.add_job("UI polish", 5)
    sched.add_job("DB backup", 10)
    print("Activity 6 release order:", sched.run_scheduler())

    # Extra edge-case checks (empty, single element, duplicates, random)
    rand_list = [random.randint(1, 100) for _ in range(15)]
    print("Random sorted check:", heap_sort(rand_list) == sorted(rand_list))
    print("Single element min-heap:", [MinHeap().insert(8) or MinHeap()])
    s_heap = MinHeap()
    s_heap.insert(8)
    print("Single element extract:", s_heap.extract())