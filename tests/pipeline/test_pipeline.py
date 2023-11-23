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

    node = Node.create(node_name)

    assert os.path.exists(node.get_file())
    assert Node.get(node_name) == node


def test_create_run(temp_catalog_dir):
    Node.create("node1").create_run("run1")
    Node.create("node2").create_run("run2")

    node_name = "test_node"
    run_name = "test_run"
    inputs = {
        "input1": {"node": "node1", "run": "run1", "file": "input1"},
        "input2": {"node": "node2", "run": "run2", "file": "input2"},
    }
    params = {"param1": "value1", "param2": "value2"}
    kernel_name = "python3"
    timeout = 600

    node = Node.create(node_name)
    run = node.create_run(run_name, inputs, params, kernel_name, timeout)

    assert os.path.exists(run.get_dir())
    assert Run.get(node_name, run_name) == run
