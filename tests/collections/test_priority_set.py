import pytest

from omisoshiru.collections import PrioritySet


def create_priority_set(equality_check, ascending):
    """
    Helper function to create a PrioritySet with specified parameters.
    """
    return PrioritySet(equality_check=equality_check, ascending=ascending)


def test_add_elements_in_ascending_order():
    pq = create_priority_set(lambda x, y: x == y, ascending=True)
    pq.add(3, "apple")
    pq.add(1, "banana")
    pq.add(2, "orange")
    assert pq.items() == [(1, "banana"), (2, "orange"), (3, "apple")]


def test_pop_element_in_ascending_order():
    pq = create_priority_set(lambda x, y: x == y, ascending=True)
    pq.add(3, "apple")
    pq.add(1, "banana")
    pq.add(2, "orange")
    popped_item = pq.pop()
    assert popped_item == (1, "banana")
    assert pq.items() == [(2, "orange"), (3, "apple")]


def test_custom_equality_check_does_not_replace_existing_item():
    custom_eq_check = lambda x, y: len(x) == len(y)
    pq = create_priority_set(custom_eq_check, ascending=True)
    pq.add(3, "apple")
    pq.add(1, "banana")
    # This should NOT replace the existing item in the queue
    pq.add(2, "orange")
    assert pq.items() == [(1, "banana"), (3, "apple")]
    # This should replace the existing item in the queue
    pq.add(2, "lemon")
    assert pq.items() == [(1, "banana"), (2, "lemon")]


def test_add_elements_in_descending_order():
    pq = create_priority_set(lambda x, y: x == y, ascending=False)
    pq.add(3, "apple")
    pq.add(1, "banana")
    pq.add(2, "orange")
    assert pq.items() == [(3, "apple"), (2, "orange"), (1, "banana")]


def test_pop_element_in_descending_order():
    pq = create_priority_set(lambda x, y: x == y, ascending=False)
    pq.add(3, "apple")
    pq.add(1, "banana")
    pq.add(2, "orange")
    popped_item = pq.pop()
    assert popped_item == (3, "apple")
    assert pq.items() == [(2, "orange"), (1, "banana")]


def test_custom_equality_check_descending_does_not_replace_existing_item():
    custom_eq_check = lambda x, y: len(x) == len(y)
    pq = create_priority_set(custom_eq_check, ascending=False)
    pq.add(3, "apple")
    pq.add(1, "banana")
    # This should NOT replace the existing item in the queue
    pq.add(2, "lemon")
    assert pq.items() == [(3, "apple"), (1, "banana")]
    # This should replace the existing item in the queue
    pq.add(2, "orange")
    assert pq.items() == [(3, "apple"), (2, "orange")]


def test_bool_method_for_empty_priority_set():
    pq_empty = create_priority_set(lambda x, y: x == y, ascending=True)
    assert not pq_empty


def test_bool_method_for_non_empty_priority_set():
    pq_non_empty = create_priority_set(lambda x, y: x == y, ascending=True)
    pq_non_empty.add(1, "apple")
    assert pq_non_empty


def test_add_same_priority_elements():
    pq = create_priority_set(lambda x, y: x == y, ascending=True)
    pq.add(3, "apple")
    pq.add(3, "banana")  # Adding an element with the same priority
    assert pq.items() == [(3, "apple"), (3, "banana")]


def test_add_elements_in_mixed_order():
    pq = create_priority_set(lambda x, y: x == y, ascending=True)
    pq.add(3, "apple")
    pq.add(1, "banana")
    pq.add(2, "orange")
    pq.add(2, "lemon")
    pq.add(3, "kiwi")
    pq.add(1, "grape")
    assert pq.items() == [
        (1, "banana"),
        (1, "grape"),
        (2, "lemon"),
        (2, "orange"),
        (3, "apple"),
        (3, "kiwi"),
    ]


def test_add_returns_true_for_successful_addition():
    pq = create_priority_set(lambda x, y: x == y, ascending=True)
    result = pq.add(3, "apple")
    assert result is True


def test_add_returns_false_for_duplicate_item():
    pq = create_priority_set(lambda x, y: x == y, ascending=True)
    pq.add(3, "apple")
    result = pq.add(4, "apple")  # Adding an element with the same priority
    assert result is False


def test_add_returns_true_for_replacing_existing_item():
    custom_eq_check = lambda x, y: len(x) == len(y)
    pq = create_priority_set(custom_eq_check, ascending=True)
    pq.add(3, "banana")
    pq.add(1, "apple")
    result = pq.add(2, "orange")
    assert result is True


if __name__ == "__main__":
    pytest.main()
