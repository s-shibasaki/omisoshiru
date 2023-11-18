import pytest

from omisoshiru.algorithm import HeapQueue


def test_heap_queue_push_and_pop():
    queue = HeapQueue()
    assert not queue
    assert len(queue) == 0
    queue.push(3, "item3")
    assert queue
    assert len(queue) == 1
    queue.push(1, "item1")
    assert queue
    assert len(queue) == 2
    queue.push(2, "item2")
    assert queue
    assert len(queue) == 3
    assert queue.pop() == (1, "item1")
    assert len(queue) == 2
    assert queue.pop() == (2, "item2")
    assert len(queue) == 1
    assert queue.pop() == (3, "item3")
    assert not queue
    assert len(queue) == 0


def test_heap_queue_empty_pop():
    queue = HeapQueue()
    assert not queue
    assert len(queue) == 0
    with pytest.raises(IndexError):
        queue.pop()
    assert not queue
    assert len(queue) == 0


if __name__ == "__main__":
    pytest.main()
