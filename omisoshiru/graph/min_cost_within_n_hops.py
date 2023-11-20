from collections import deque
from typing import Any, Literal, Optional

import networkx as nx

from ..collections import PrioritySet, remove_item_from_deque


def min_cost_within_n_hops(
    graph: nx.Graph,
    source_node: Any,
    max_hops: Optional[int] = 5,
    cost_type: Optional[Literal["cost", "weight"]] = "cost",
) -> PrioritySet:
    """
    Finds the minimum cost paths within a specified number of hops from a source node in a graph.

    Args:
        graph (nx.Graph): The input graph.
        source_node (Any): The source node to start the traversal.
        max_hops (Optional[int]): The maximum number of hops to consider. Defaults to 5.
        cost_type (Optional[Literal]): The type of cost to consider.
            Valid values are "cost" or "weight". Defaults to "cost".

    Returns:
        PrioritySet: A PrioritySet containing the nodes visited in the order of their minimum costs.
    """
    # Validate cost_type
    valid_cost_types = ["cost", "weight"]
    if cost_type not in valid_cost_types:
        raise ValueError(
            f"Invalid cost_type. Valid values are: {', '.join(valid_cost_types)}"
        )

    # Determine priority order and cost calculation based on cost_type
    ascending_order = True if cost_type == "cost" else False
    cost_calculation = lambda x, y: x + y if cost_type == "cost" else x * y
    initial_cost = 0 if cost_type == "cost" else 1

    # Initialize the queue with the source node
    hop_cost_node_queue = deque()
    hop_cost_node_queue.append((0, initial_cost, source_node))  # hop, cost, node

    # Initialize the priority set
    priority_set = PrioritySet(
        equality_check=lambda x, y: x == y,
        ascending=ascending_order,
    )
    priority_set.add(initial_cost, source_node)

    # Process nodes in the queue
    while hop_cost_node_queue:
        current_hop, current_cost, current_node = hop_cost_node_queue.popleft()

        # Explore neighboring nodes
        edges = graph.edges(current_node, data=True)
        for _, next_node, data in edges:
            next_hop = current_hop + 1
            next_cost = cost_calculation(current_cost, data[cost_type])

            # Add the next node to the priority set if it has not been visited
            # and the maximum hop limit has not been reached
            succeed, removed = priority_set.add(next_cost, next_node)
            if removed:
                remove_item_from_deque(
                    hop_cost_node_queue, lambda x: x[2] == removed[1]
                )
            if succeed and next_hop < max_hops:
                hop_cost_node_queue.append((next_hop, next_cost, next_node))

    return priority_set
