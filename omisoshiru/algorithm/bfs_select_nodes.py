from collections import deque


def bfs_select_nodes(graph, start_node, target_count):
    visited = set()
    queue = deque([start_node])
    selected_nodes = []

    while queue and len(selected_nodes) < target_count:
        current_node = queue.popleft()

        if current_node not in visited:
            visited.add(current_node)
            selected_nodes.append(current_node)

            neighbors = list(graph.neighbors(current_node))
            queue.extend(neighbors)

    return selected_nodes
