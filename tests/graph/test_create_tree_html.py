import os

import networkx as nx
import pytest

from omisoshiru.graph.create_tree_html import create_tree_html

# Test data
test_graph = nx.MultiDiGraph()
test_graph.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)])
test_root_node = 1
test_output_file = "test_output_tree.html"


def test_create_tree_html():
    # Temporary output file path for testing
    test_output_path = os.path.join(os.path.dirname(__file__), test_output_file)

    # Call the function with test data
    create_tree_html(test_graph, test_root_node, test_output_path)

    # Check if the output file exists
    assert os.path.exists(test_output_path)

    # After the tests are done, remove the temporary output file
    os.remove(test_output_path)
