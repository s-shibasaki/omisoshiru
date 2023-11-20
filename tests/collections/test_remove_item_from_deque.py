from collections import deque

import pytest

from omisoshiru.collections import remove_item_from_deque


def test_remove_even_numbers_from_deque():
    deque_obj = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
    condition_func = lambda x: x % 2 == 0
    result = remove_item_from_deque(deque_obj, condition_func)
    assert result == deque([1, 3, 5, 7, 9])


def test_remove_items_divisible_by_3_from_deque():
    deque_obj = deque([10, 15, 20, 25, 30, 35, 40])
    condition_func = lambda x: x % 3 == 0
    result = remove_item_from_deque(deque_obj, condition_func)
    assert result == deque([10, 20, 25, 35, 40])


def test_remove_items_with_length_greater_than_3_from_deque():
    deque_obj = deque(["apple", "banana", "fig", "pear", "grape"])
    condition_func = lambda x: len(x) > 3
    result = remove_item_from_deque(deque_obj, condition_func)
    assert result == deque(["fig"])


def test_remove_items_containing_letter_a_from_deque():
    deque_obj = deque(["cat", "dog", "bird", "snake"])
    condition_func = lambda x: "a" in x
    result = remove_item_from_deque(deque_obj, condition_func)
    assert result == deque(["dog", "bird"])


def test_remove_all_items_from_empty_deque():
    deque_obj = deque([])
    condition_func = lambda x: True  # Remove all items
    result = remove_item_from_deque(deque_obj, condition_func)
    assert result == deque([])


if __name__ == "__main__":
    pytest.main()
