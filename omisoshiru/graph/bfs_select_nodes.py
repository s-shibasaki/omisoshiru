# omisoshiru/graph/bfs_select_nodes.py

from typing import Any, List

import networkx as nx


def bfs_select_nodes(graph: nx.Graph, start_node: Any, target_count: int) -> List[Any]:
    """
    Perform Breadth-First Search (BFS) on a graph to select a specified number of nodes.

    Args:
        graph (networkx.Graph): The input graph (NetworkX Graph object).
        start_node (Any): The starting node for BFS.
        target_count (int): The number of nodes to be selected.

    Returns:
        List[Any]: A list of selected nodes.

    Example:
        >>> import networkx as nx
        >>> graph = nx.Graph()
        >>> graph.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)])
        >>> start_node = 1
        >>> target_count = 3
        >>> bfs_select_nodes(graph, start_node, target_count)
        [1, 2, 3]
    """
    visited = set()
    queue = [start_node]
    selected_nodes = []

    while queue and len(selected_nodes) < target_count:
        current_node = queue.pop(0)

        if current_node not in visited:
            visited.add(current_node)
            selected_nodes.append(current_node)

            neighbors = list(graph.neighbors(current_node))
            queue.extend(neighbors)

    return selected_nodes
