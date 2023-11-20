import pytest

from omisoshiru.collections.priority_set import PrioritySet


def test_priority_set_add_overwrite_higher_priority():
    priority_set = PrioritySet(ascending=True)

    assert priority_set.add(3, "apple") == True
    assert priority_set.add(4, "banana") == True
    assert priority_set.add(2, "orange") == True

    # Higher priority, should overwrite
    assert priority_set.add(1, "banana") == True
    assert priority_set.items() == [(1, "banana"), (2, "orange"), (3, "apple")]


def test_priority_set_add_overwrite_lower_priority():
    priority_set = PrioritySet(ascending=True)

    assert priority_set.add(3, "apple") == True
    assert priority_set.add(4, "banana") == True
    assert priority_set.add(2, "orange") == True

    # Same priority, should not overwrite
    assert priority_set.add(5, "banana") == False
    assert priority_set.items() == [(2, "orange"), (3, "apple"), (4, "banana")]


def test_priority_set_add_overwrite_higher_priority_descending():
    priority_set = PrioritySet(ascending=False)

    assert priority_set.add(3, "apple") == True
    assert priority_set.add(4, "banana") == True
    assert priority_set.add(2, "orange") == True

    # Higher priority, should overwrite
    assert priority_set.add(5, "banana") == True
    assert priority_set.items() == [(5, "banana"), (3, "apple"), (2, "orange")]


def test_priority_set_add_overwrite_lower_priority_descending():
    priority_set = PrioritySet(ascending=False)

    assert priority_set.add(3, "apple") == True
    assert priority_set.add(4, "banana") == True
    assert priority_set.add(2, "orange") == True

    # Same priority, should not overwrite
    assert priority_set.add(1, "banana") == False
    assert priority_set.items() == [(4, "banana"), (3, "apple"), (2, "orange")]


def test_priority_set_pop():
    priority_set = PrioritySet(ascending=True)

    priority_set.add(3, "apple")
    priority_set.add(1, "banana")
    priority_set.add(2, "orange")

    assert priority_set.pop() == (1, "banana")
    assert priority_set.items() == [(2, "orange"), (3, "apple")]


def test_priority_set_pop_descending():
    priority_set = PrioritySet(ascending=False)

    priority_set.add(3, "apple")
    priority_set.add(1, "banana")
    priority_set.add(2, "orange")

    assert priority_set.pop() == (3, "apple")
    assert priority_set.items() == [(2, "orange"), (1, "banana")]


def test_priority_set_items():
    priority_set = PrioritySet(ascending=True)

    priority_set.add(3, "apple")
    priority_set.add(1, "banana")
    priority_set.add(2, "orange")

    assert priority_set.items() == [(1, "banana"), (2, "orange"), (3, "apple")]


def test_priority_set_items_descending():
    priority_set = PrioritySet(ascending=False)

    priority_set.add(3, "apple")
    priority_set.add(1, "banana")
    priority_set.add(2, "orange")

    assert priority_set.items() == [(3, "apple"), (2, "orange"), (1, "banana")]


def test_priority_set_bool():
    priority_set = PrioritySet(ascending=True)

    assert bool(priority_set) == False

    priority_set.add(3, "apple")

    assert bool(priority_set) == True


def test_priority_set_iteration():
    priority_set = PrioritySet(ascending=True)

    priority_set.add(3, "apple")
    priority_set.add(1, "banana")
    priority_set.add(2, "orange")

    result = list(iter(priority_set))

    assert result == [(1, "banana"), (2, "orange"), (3, "apple")]


def test_priority_set_iteration_descending():
    priority_set = PrioritySet(ascending=False)

    priority_set.add(3, "apple")
    priority_set.add(1, "banana")
    priority_set.add(2, "orange")

    result = list(iter(priority_set))

    assert result == [(3, "apple"), (2, "orange"), (1, "banana")]
