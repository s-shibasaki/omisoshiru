from collections import deque


def remove_item_from_deque(deque_obj, condition_func):
    """
    Remove items from a deque based on a custom condition.

    Args:
        deque_obj (deque): The deque from which items should be removed.
        condition_func (Callable): A callable that takes an item and returns a boolean indicating whether the item should be removed.

    Returns:
        deque: The modified deque with items removed based on the specified condition.
    """
    filtered_data = deque(item for item in deque_obj if not condition_func(item))
    deque_obj.clear()
    deque_obj.extend(filtered_data)
    return deque_obj
