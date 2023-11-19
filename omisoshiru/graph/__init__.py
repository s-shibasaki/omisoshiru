"""
Graph-related utilities and algorithms.

This module provides utilities and algorithms for working with graphs using the networkx library.

Available functions:
    - bfs_select_nodes: Perform Breadth-First Search (BFS) on a graph to select a specified number of nodes.

Example:
    >>> import networkx as nx
    >>> from omisoshiru.graph import bfs_select_nodes
    >>> # Create a simple undirected graph
    >>> graph = nx.Graph()
    >>> graph.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 5), (4, 5)])
    >>> start_node = 1
    >>> target_count = 3
    >>> bfs_select_nodes(graph, start_node, target_count)
    [1, 2, 3]
"""

from .bfs_select_nodes import bfs_select_nodes

__all__ = ["bfs_select_nodes"]
