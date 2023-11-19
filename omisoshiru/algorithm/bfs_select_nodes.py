from collections import deque
from typing import Any, List, Set


def bfs_select_nodes(graph: Any, start_node: Any, target_count: int) -> List[Any]:
    """
    Perform Breadth-First Search (BFS) on a graph to select a specified number of nodes.

    Args:
        graph (Any): The input graph.
        start_node (Any): The starting node for BFS.
        target_count (int): The number of nodes to be selected.

    Returns:
        List[Any]: A list of selected nodes.

    Example:
        >>> graph = {...}  # Your graph implementation here
        >>> start_node = 1  # Your starting node here
        >>> target_count = 3
        >>> bfs_select_nodes(graph, start_node, target_count)
        [1, 2, 3]
    """
    visited: Set[Any] = set()
    queue = deque([start_node])
    selected_nodes: List[Any] = []

    while queue and len(selected_nodes) < target_count:
        current_node = queue.popleft()

        if current_node not in visited:
            visited.add(current_node)
            selected_nodes.append(current_node)

            neighbors = list(graph.neighbors(current_node))
            queue.extend(neighbors)

    return selected_nodes
