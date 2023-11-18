import heapq


class HeapQueue:
    def __init__(self):
        self.h = []

    def push(self, value, item):
        heapq.heappush(self.h, (value, item))

    def pop(self):
        return heapq.heappop(self.h)

    def __len__(self):
        return len(self.h)

    def __bool__(self):
        return bool(self.h)
