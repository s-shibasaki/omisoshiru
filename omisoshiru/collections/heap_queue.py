import heapq
from typing import Any, List, Tuple


class HeapQueue:
    def __init__(self) -> None:
        """
        A priority queue implementation using the heapq module.

        Example:
            >>> priority_queue = HeapQueue()
            >>> priority_queue.push(3, 'apple')
            >>> priority_queue.push(1, 'banana')
            >>> priority_queue.push(2, 'orange')
            >>> priority_queue.items()
            [(1, 'banana'), (3, 'apple'), (2, 'orange')]
            >>> priority_queue.pop()
            (1, 'banana')
            >>> len(priority_queue)
            2
            >>> bool(priority_queue)
            True
        """
        self._heap: List[Tuple[int, Any]] = []

    def push(self, value: int, item: Any) -> None:
        """
        Pushes an element with its priority value onto the heap.

        Args:
            value (int): The priority value of the element.
            item (Any): The element to be added.

        Returns:
            None
        """
        heapq.heappush(self._heap, (value, item))

    def pop(self) -> Tuple[int, Any]:
        """
        Pops and returns the element with the highest priority from the heap.

        Returns:
            Tuple[int, Any]: The element with the highest priority.
        """
        return heapq.heappop(self._heap)

    def __len__(self) -> int:
        """
        Returns the number of elements in the heap.

        Returns:
            int: The number of elements in the heap.
        """
        return len(self._heap)

    def __bool__(self) -> bool:
        """
        Returns True if the heap is non-empty, False otherwise.

        Returns:
            bool: True if the heap is non-empty, False otherwise.
        """
        return bool(self._heap)

    def items(self) -> List[Tuple[int, Any]]:
        """
        Returns a list of elements in the heap.

        Returns:
            List[Tuple[int, Any]]: List of elements in the heap.
        """
        return self._heap
