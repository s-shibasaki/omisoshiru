import bisect
from typing import Callable, Any

class PrioritySet:
    def __init__(self, equality_check: Callable[[Any], bool]):
        self._data = []
        self.equality_check = equality_check

    def add(self, value, item):
        for i, existing in enumerate(self._data):
            if self.equality_check(item, existing[1]):
                j = bisect.bisect(self._data, (value, item))
                if j <= i:
                    del self._data[i]
                    self._data.insert(j, (value, item))
                break
        else:
            bisect.insort(self._data, (value, item))

    def pop(self):
        return self._data.pop(0)
    
    def items(self):
        return self._data