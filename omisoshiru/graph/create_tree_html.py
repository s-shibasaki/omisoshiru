import networkx as nx
from pyvis.network import Network

from ..collections import HeapQueue


def create_tree_html(
    graph, root_node, output_file, max_depth=5, max_nodes=100, gravity=-50
):
    """
    Create a tree from a multi-edge graph and output it as an HTML file.

    Parameters:
        graph (nx.Graph): Multi-edge graph.
            The input graph from which the tree will be generated.
        root_node (int): Root node for the tree.
            The starting node for the tree generation.
        output_file (str): Output HTML file name.
            The name of the HTML file where the tree visualization will be saved.
        max_depth (int, optional): Maximum depth for tree generation.
            The maximum depth for the tree generation (default is 5).
        max_nodes (int, optional): Maximum number of nodes in the tree.
            The maximum number of nodes to include in the generated tree (default is 100).
        gravity (int, optional): Gravity parameter for the force-directed layout.
            Adjusting gravity can affect the layout of the tree (default is -50).

    Returns:
        None

    Notes:
        This function uses a BFS-based approach to generate a tree from the input
        multi-edge graph and visualizes it using the Pyvis library. The resulting
        HTML file contains an interactive tree visualization.

    Example:
        # Sample graph creation
        G = nx.MultiDiGraph()
        G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)])

        # Create tree and output as HTML
        create_tree_html(G, 1, "output_tree.html")
    """
    # Initialize HeapQueue and subgraph
    queue = HeapQueue(ascending=False)
    subgraph = nx.Graph()
    queue.push(1, (0, root_node, None, None))

    # Build the tree using BFS
    while queue and subgraph.number_of_nodes() < max_nodes:
        weight, (depth, node, parent, label) = queue.pop()
        if parent is not None and not subgraph.has_node(node):
            subgraph.add_edge(parent, node, label=label, weight=(weight * 10))
        if depth < max_depth:
            neighbors = graph.neighbors(node)
            for neighbor in neighbors:
                data = [
                    __data
                    for __x, __y, __data in graph.edges(node, data=True)
                    if __y == neighbor
                ]
                label = "\n\n".join(
                    [
                        f"[link {i}]\n"
                        + "\n".join([f"{k}: {v}" for k, v in data.items()])
                        for i, data in enumerate(data)
                    ]
                )
                weight = max([data["weight"] if 'weight' in data else 1 for data in data])
                queue.push(weight, (depth + 1, neighbor, node, label))

    g = Network(
        "calc(100vh - 10px)", "calc(100vw - 6px)", notebook=True, cdn_resources="remote"
    )
    g.from_nx(subgraph)
    g.force_atlas_2based(gravity)
    g.write_html(output_file)
