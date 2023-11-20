import bisect
from typing import Any, Callable, Optional


class PrioritySet:
    def __init__(
        self,
        equality_check: Optional[Callable[[Any, Any], bool]] = None,
        ascending: bool = True,
    ) -> None:
        """
        A priority set implementation that maintains a sorted set of unique elements based on their priority values.

        Args:
            equality_check (Optional[Callable[[Any, Any], bool]]): A callable that determines equality between two elements.
                Defaults to None, in which case the default equality function (x == y) is used.
            ascending (bool): If True, the priority set will be in ascending order; if False, in descending order.

        Example:
            >>> priority_set = PrioritySet(lambda x, y: x == y, ascending=True)
            >>> priority_set.add(3, 'apple')
            >>> priority_set.add(1, 'banana')
            >>> priority_set.add(2, 'orange')
            >>> priority_set.items()
            [(1, 'banana'), (2, 'orange'), (3, 'apple')]
            >>> priority_set.pop()
            (1, 'banana')
            >>> priority_set.items()
            [(2, 'orange'), (3, 'apple')]
        """
        self._data = []
        self._equality_check = equality_check or (lambda x, y: x == y)
        self._ascending = ascending

    def add(self, value: Any, item: Any) -> bool:
        """
        Adds an element with its priority value to the priority set.

        Args:
            value (Any): The priority value of the element.
            item (Any): The element to be added.

        Returns:
            bool: True if the element was added, False if not (due to equality condition).
        """
        if not self._ascending:
            value = -value  # Invert the value back for descending order

        for i, existing in enumerate(self._data):
            if self._equality_check(item, existing[1]):
                j = bisect.bisect(self._data, (value, item))
                if j <= i:
                    del self._data[i]
                    self._data.insert(j, (value, item))
                    return True
                else:
                    return False
        else:
            bisect.insort(self._data, (value, item))
            return True

    def pop(self) -> Any:
        """
        Removes and returns the element with the highest priority.

        Returns:
            Any: The element with the highest priority.
        """
        value, item = self._data.pop(0)
        if not self._ascending:
            value = -value  # Invert the value back for descending order
        return value, item

    def items(self) -> list:
        """
        Returns a list of elements in the priority set.

        Returns:
            list: List of elements in the priority set.
        """
        if self._ascending:
            return self._data
        else:
            # Invert the values back for descending order
            return [(-value, item) for value, item in self._data]

    def __bool__(self) -> bool:
        """
        Returns True if the priority set is non-empty, False otherwise.

        Returns:
            bool: True if the priority set is non-empty, False otherwise.
        """
        return bool(self._data)
