import networkx as nx
import pytest

from omisoshiru.graph import min_cost_within_n_hops


def test_min_cost_within_n_hops_cost_type_cost():
    graph = nx.Graph()
    graph.add_edge(1, 2, cost=1)
    graph.add_edge(2, 3, cost=2)
    graph.add_edge(1, 4, cost=4)

    result = min_cost_within_n_hops(
        graph, source_node=1, max_hops=2, cost_type="cost", max_nodes=None
    )
    assert result.items() == [(0, 1), (1, 2), (3, 3), (4, 4)]


def test_min_cost_within_n_hops_cost_type_weight():
    graph = nx.Graph()
    graph.add_edge(1, 2, weight=0.5)
    graph.add_edge(2, 3, weight=0.1)
    graph.add_edge(1, 4, weight=0.9)

    result = min_cost_within_n_hops(
        graph, source_node=1, max_hops=2, cost_type="weight", max_nodes=None
    )
    assert result.items() == [(1, 1), (0.9, 4), (0.5, 2), (0.05, 3)]


def test_min_cost_within_n_hops_invalid_cost_type():
    graph = nx.Graph()

    # Ensure ValueError is raised for invalid cost_type
    with pytest.raises(ValueError, match="Invalid cost_type"):
        min_cost_within_n_hops(
            graph, source_node=1, max_hops=2, cost_type="invalid", max_nodes=None
        )


def test_min_cost_within_n_hops_max_hops_reached():
    graph = nx.Graph()
    graph.add_edge(1, 2, cost=1)
    graph.add_edge(2, 3, cost=2)
    graph.add_edge(1, 4, cost=4)

    result = min_cost_within_n_hops(
        graph, source_node=1, max_hops=1, cost_type="cost", max_nodes=None
    )
    assert result.items() == [(0, 1), (1, 2), (4, 4)]


def test_min_cost_within_n_hops_single_node():
    graph = nx.Graph()
    graph.add_node(1)

    # Ensure the PrioritySet contains only the source node
    result = min_cost_within_n_hops(
        graph, source_node=1, max_hops=2, cost_type="cost", max_nodes=None
    )
    assert result.items() == [(0, 1)]


def test_min_cost_within_n_hops_multiple_edges():
    graph = nx.Graph()
    graph.add_edge(1, 2, cost=5)
    graph.add_edge(1, 3, cost=2)
    graph.add_edge(2, 3, cost=1)
    graph.add_edge(3, 4, cost=3)
    graph.add_edge(3, 4, cost=2)

    result = min_cost_within_n_hops(
        graph, source_node=1, max_hops=2, cost_type="cost", max_nodes=None
    )
    assert result.items() == [(0, 1), (2, 3), (3, 2), (4, 4)]


def test_min_cost_within_n_hops_negative_costs():
    graph = nx.Graph()
    graph.add_edge(1, 2, cost=-1)
    graph.add_edge(2, 3, cost=-2)
    graph.add_edge(1, 4, cost=-4)

    result = min_cost_within_n_hops(
        graph, source_node=1, max_hops=2, cost_type="cost", max_nodes=None
    )
    assert result.items() == [(-8, 1), (-4, 4), (-3, 3), (-1, 2)]


def test_min_cost_within_n_hops_with_max_nodes():
    graph = nx.Graph()
    graph.add_edge(1, 2, cost=5)
    graph.add_edge(1, 3, cost=2)
    graph.add_edge(1, 4, cost=4)
    graph.add_edge(2, 3, cost=1)

    result = min_cost_within_n_hops(
        graph, source_node=1, max_hops=2, cost_type="cost", max_nodes=3
    )
    assert result.items() == [(0, 1), (2, 3), (3, 2)]
