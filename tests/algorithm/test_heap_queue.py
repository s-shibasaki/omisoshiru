from omisoshiru.algorithm.heap_queue import HeapQueue

def test_push_and_pop():
    heap_queue = HeapQueue()
    heap_queue.push(3, 'apple')
    heap_queue.push(1, 'banana')
    heap_queue.push(2, 'orange')

    assert heap_queue.pop() == (1, 'banana')
    assert heap_queue.pop() == (2, 'orange')
    assert heap_queue.pop() == (3, 'apple')

def test_len_and_bool():
    heap_queue = HeapQueue()
    assert len(heap_queue) == 0
    assert not heap_queue

    heap_queue.push(5, 'grape')
    assert len(heap_queue) == 1
    assert heap_queue

def test_items():
    heap_queue = HeapQueue()
    heap_queue.push(3, 'apple')
    heap_queue.push(1, 'banana')
    heap_queue.push(2, 'orange')

    assert heap_queue.items() == [(1, 'banana'), (3, 'apple'), (2, 'orange')]
