import pytest

from omisoshiru.collections import PrioritySet


def test_add():
    pq = PrioritySet(lambda x, y: x == y, ascending=True)

    pq.add(3, "apple")
    pq.add(1, "banana")
    pq.add(2, "orange")

    assert pq.items() == [(1, "banana"), (2, "orange"), (3, "apple")]


def test_pop():
    pq = PrioritySet(lambda x, y: x == y, ascending=True)

    pq.add(3, "apple")
    pq.add(1, "banana")
    pq.add(2, "orange")

    popped_item = pq.pop()

    assert popped_item == (1, "banana")
    assert pq.items() == [(2, "orange"), (3, "apple")]


def test_custom_equality_check():
    # Custom equality check function: Compare the lengths of strings
    custom_eq_check = lambda x, y: len(x) == len(y)
    pq = PrioritySet(custom_eq_check, ascending=True)

    pq.add(3, "apple")
    pq.add(1, "banana")

    # This should NOT replace the existing item in the queue
    pq.add(2, "orange")
    assert pq.items() == [(1, "banana"), (3, "apple")]

    # This should replace the existing item in the queue
    pq.add(2, "lemon")
    assert pq.items() == [(1, "banana"), (2, "lemon")]


def test_add_descending():
    pq = PrioritySet(lambda x, y: x == y, ascending=False)

    pq.add(3, "apple")
    pq.add(1, "banana")
    pq.add(2, "orange")

    assert pq.items() == [(3, "apple"), (2, "orange"), (1, "banana")]


def test_pop_descending():
    pq = PrioritySet(lambda x, y: x == y, ascending=False)

    pq.add(3, "apple")
    pq.add(1, "banana")
    pq.add(2, "orange")

    popped_item = pq.pop()

    assert popped_item == (3, "apple")
    assert pq.items() == [(2, "orange"), (1, "banana")]


def test_custom_equality_check_descending():
    # Custom equality check function: Compare the lengths of strings
    custom_eq_check = lambda x, y: len(x) == len(y)
    pq = PrioritySet(custom_eq_check, ascending=False)

    pq.add(3, "apple")
    pq.add(1, "banana")

    # This should NOT replace the existing item in the queue
    pq.add(2, "lemon")
    assert pq.items() == [(3, "apple"), (1, "banana")]

    # This should replace the existing item in the queue
    pq.add(2, "orange")
    assert pq.items() == [(3, "apple"), (2, "orange")]


if __name__ == "__main__":
    pytest.main()
