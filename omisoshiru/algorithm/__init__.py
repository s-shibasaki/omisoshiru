from .bfs_select_nodes import bfs_select_nodes
from .heap_queue import HeapQueue
from .partial_match import partial_match
from .priority_set import PrioritySet

__all__ = [
    "bfs_select_nodes",
    "HeapQueue",
    "partial_match",
    "PrioritySet",
]

"""
Algorithms Package

This package contains various algorithms implemented for common use cases.

Modules:
- bfs_select_nodes: Breadth-First Search (BFS) algorithm for selecting nodes in a graph.
- heap_queue: Priority queue implementation using the heapq module.
- partial_match: Function for finding partial matches of patterns in a target list.
- priority_set: Priority set implementation for maintaining a sorted set of unique elements.

Example:
    >>> from omisoshiru.algorithm import bfs_select_nodes, HeapQueue, partial_match, PrioritySet
    >>> # Use the algorithms in your application
"""
