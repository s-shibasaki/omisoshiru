import heapq


class HeapQueue:
    def __init__(self):
        self.__h = []

    def push(self, value, item):
        heapq.heappush(self.__h, (value, item))

    def pop(self):
        return heapq.heappop(self.__h)

    def __len__(self):
        return len(self.__h)

    def __bool__(self):
        return bool(self.__h)

    def items(self):
        return self.__h