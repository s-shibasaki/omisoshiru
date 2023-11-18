import pytest
from omisoshiru.algorithm import PriorityQueue

def test_add():
    pq = PriorityQueue(lambda x, y: x == y)

    pq.add(3, 'apple')
    pq.add(1, 'banana')
    pq.add(2, 'orange')

    assert pq.items() == [(1, 'banana'), (2, 'orange'), (3, 'apple')]

def test_pop():
    pq = PriorityQueue(lambda x, y: x == y)

    pq.add(3, 'apple')
    pq.add(1, 'banana')
    pq.add(2, 'orange')

    popped_item = pq.pop()

    assert popped_item == (1, 'banana')
    assert pq.items() == [(2, 'orange'), (3, 'apple')]

def test_custom_equality_check():
    # Custom equality check function: Compare the lengths of strings
    custom_eq_check = lambda x, y: len(x) == len(y)
    pq = PriorityQueue(custom_eq_check)

    pq.add(3, 'apple')
    pq.add(1, 'banana')

    # This should NOT replace the existing item in the queue
    pq.add(2, 'orange')
    assert pq.items() == [(1, 'banana'), (3, 'apple')]

    # This should replace the existing item in the queue
    pq.add(2, 'lemon')
    assert pq.items() == [(1, 'banana'), (2, 'lemon')]


if __name__ == "__main__":
    pytest.main()
