"""
Collection of custom data structures and algorithms.

This module provides custom implementations of data structures and algorithms for various purposes.

Available classes:
    - HeapQueue: A priority queue implementation using the heapq module.
    - PrioritySet: A priority set implementation that maintains a sorted set of unique elements based on their priority values.

Example:
    >>> from omisoshiru.collections import HeapQueue, PrioritySet
    >>> pq = HeapQueue()
    >>> pq.push(3, 'apple')
    >>> pq.push(1, 'banana')
    >>> pq.push(2, 'orange')
    >>> pq.items()
    [(1, 'banana'), (3, 'apple'), (2, 'orange')]
    >>> ps = PrioritySet(lambda x, y: x == y)
    >>> ps.add(3, 'apple')
    >>> ps.add(1, 'banana')
    >>> ps.add(2, 'orange')
    >>> ps.items()
    [(1, 'banana'), (2, 'orange'), (3, 'apple')]
"""

from .heap_queue import HeapQueue
from .priority_set import PrioritySet

__all__ = [
    "HeapQueue",
    "PrioritySet",
]
