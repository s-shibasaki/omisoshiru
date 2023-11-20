import bisect
from typing import Any, Callable, Optional, Tuple


class PrioritySet:
    def __init__(
        self,
        equality_check: Optional[Callable[[Any, Any], bool]] = None,
        ascending: bool = True,
        max_size: Optional[int] = None,
    ) -> None:
        """
        A priority set implementation that maintains a sorted set of unique elements based on their priority values.

        Args:
            equality_check (Optional[Callable[[Any, Any], bool]]): A callable that determines equality between two elements.
                Defaults to None, in which case the default equality function (x == y) is used.
            ascending (bool): If True, the priority set will be in ascending order; if False, in descending order.
            max_size (Optional[int]): The maximum number of elements the priority set can hold. Defaults to None.

        Example:
            >>> priority_set = PrioritySet(lambda x, y: x == y, ascending=True, max_size=5)
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
        self._max_size = max_size

    def _truncation(self):
        if self._max_size is not None and len(self._data) > self._max_size:
            removed_value, removed_item = self._data.pop()
            if not self._ascending:
                removed_value = -removed_value
            return removed_value, removed_item

    def add(self, value: Any, item: Any) -> Tuple[bool, Optional[Any]]:
        """
        Adds an element with its priority value to the priority set.

        Args:
            value (Any): The priority value of the element.
            item (Any): The element to be added.

        Returns:
            Tuple[bool, Optional[Tuple[Any, Any]]]: A tuple containing a boolean indicating whether the element was
            successfully added, and an optional tuple containing the removed element's priority value and item if
            the addition resulted in truncation due to reaching the maximum size.
        """
        if not self._ascending:
            value = -value  # Invert the value back for descending order

        j = bisect.bisect_right(self._data, (value, item))
        if self._max_size is not None and j >= self._max_size:
            return False, None
        for i, existing in enumerate(self._data):
            if self._equality_check(item, existing[1]):
                if j <= i:  # priority of new value is higher than exististing value
                    removed_value, removed_item = self._data.pop(i)
                    if not self._ascending:
                        removed_value = -removed_value
                    self._data.insert(j, (value, item))
                    return True, (removed_value, removed_item)
                else:
                    return False, None
        else:
            self._data.insert(j, (value, item))
            return True, self._truncation()

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

    def __iter__(self):
        """
        Returns an iterator for the priority set.

        Returns:
            iterator: Iterator for the priority set.
        """
        return iter(self.items())
