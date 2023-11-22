import os
from tempfile import TemporaryDirectory

import pytest

from omisoshiru.pipeline import Catalog, Node, Run


@pytest.fixture
def temp_catalog_dir():
    with TemporaryDirectory() as temp_dir:
        Catalog.set_catalog_dir(temp_dir)
        yield temp_dir


def test_create_node(temp_catalog_dir):
    node_name = "test_node"
    inputs = ["input1", "input2"]
    outputs = ["output1", "output2"]
    params = ["param1", "param2"]

    node = Node.create(node_name, inputs, outputs, params)

    assert os.path.exists(node.get_file())
    assert node.get(node_name) == node


def test_create_run(temp_catalog_dir):
    Node.create("node1", [], ["input1"], []).run("run1", {}, {})
    Node.create("node2", [], ["input2"], []).run("run2", {}, {})

    node_name = "test_node"
    run_name = "test_run"
    inputs = {
        "input1": {"node": "node1", "run": "run1", "data": "input1"},
        "input2": {"node": "node2", "run": "run2", "data": "input2"},
    }
    params = {"param1": "value1", "param2": "value2"}
    kernel_name = "python3"
    timeout = 600

    node = Node.create(node_name, inputs=[], outputs=[], params=[])
    run = Run.create(node_name, run_name, inputs, params, kernel_name, timeout)

    assert os.path.exists(run.get_dir())
    assert run.get(node_name, run_name) == run


def test_catalog_load_save(temp_catalog_dir):
    catalog = Catalog.load()

    assert catalog.nodes == []
    assert catalog.runs == []

    # Modify catalog and save
    node = Node.create("test_node", inputs=[], outputs=[], params=[])
    run = Run.create(
        "test_node", "test_run", inputs={}, params={}, kernel_name="", timeout=None
    )

    # Load catalog and check if modifications are applied
    new_catalog = Catalog.load()
    assert new_catalog.get_node("test_node") == node
    assert new_catalog.get_run("test_node", "test_run") == run
