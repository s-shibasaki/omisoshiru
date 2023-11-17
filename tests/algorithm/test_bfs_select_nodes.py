import networkx as nx
import pytest

from omisoshiru.algorithm import bfs_select_nodes


@pytest.fixture
def graph():
    graph = nx.Graph()
    graph.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (3, 5)])
    return graph


def test_bfs_select_nodes_case1(graph):
    start_node = 1
    target_count = 3
    expected_result = [1, 2, 3]
    assert bfs_select_nodes(graph, start_node, target_count) == expected_result


def test_bfs_select_nodes_case2(graph):
    start_node = 3
    target_count = 4
    expected_result = [3, 1, 4, 5]
    assert bfs_select_nodes(graph, start_node, target_count) == expected_result


def test_bfs_select_nodes_case3(graph):
    start_node = 5
    target_count = 2
    expected_result = [5, 3]
    assert bfs_select_nodes(graph, start_node, target_count) == expected_result


if __name__ == "__main__":
    pytest.main()
