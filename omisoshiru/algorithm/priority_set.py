import bisect
from typing import Callable, Any, Optional


class PrioritySet:
    """
    A priority set implementation that maintains a sorted set of unique elements based on their priority values.

    Args:
        equality_check (Optional[Callable[[Any, Any], bool]]): A callable that determines equality between two elements.
            Defaults to None, in which case the default equality function (x == y) is used.

    Attributes:
        _data (list): A list to store elements with their priority values.
        _equality_check (Callable[[Any, Any], bool]): The equality check function for comparing elements.

    Methods:
        add(value, item): Adds an element with its priority value to the priority set.
        pop(): Removes and returns the element with the highest priority.
        items(): Returns a list of elements in the priority set.

    Example:
        >>> priority_set = PrioritySet(lambda x, y: x == y)
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

    def __init__(
        self, equality_check: Optional[Callable[[Any, Any], bool]] = None
    ) -> None:
        """
        Initializes a PrioritySet instance.

        Args:
            equality_check (Optional[Callable[[Any, Any], bool]]): A callable that determines equality between two elements.
                Defaults to None, in which case the default equality function (x == y) is used.

        Returns:
            None
        """
        self._data = []
        self._equality_check = equality_check if equality_check is not None else lambda x, y: x == y

    def add(self, value: Any, item: Any) -> None:
        """
        Adds an element with its priority value to the priority set.

        Args:
            value (Any): The priority value of the element.
            item (Any): The element to be added.

        Returns:
            None
        """
        for i, existing in enumerate(self._data):
            if self._equality_check(item, existing[1]):
                j = bisect.bisect(self._data, (value, item))
                if j <= i:
                    del self._data[i]
                    self._data.insert(j, (value, item))
                break
        else:
            bisect.insort(self._data, (value, item))

    def pop(self) -> Any:
        """
        Removes and returns the element with the highest priority.

        Returns:
            Any: The element with the highest priority.
        """
        return self._data.pop(0)

    def items(self) -> list:
        """
        Returns a list of elements in the priority set.

        Returns:
            list: List of elements in the priority set.
        """
        return self._data
