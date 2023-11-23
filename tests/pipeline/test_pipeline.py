import os
import shutil
import tempfile

import pytest

from omisoshiru.pipeline import Catalog, Node, Run


@pytest.fixture
def temp_catalog_dir(request):
    catalog_dir = tempfile.mkdtemp()

    def fin():
        shutil.rmtree(catalog_dir)

    request.addfinalizer(fin)
    return catalog_dir


def test_create_node(temp_catalog_dir):
    Catalog.set_catalog_dir(temp_catalog_dir)

    # Create a node
    node_name = "test_node"
    node = Node.create(node_name)

    # Check if the node was created
    assert Node.get(node_name) == node


def test_create_run(temp_catalog_dir):
    Catalog.set_catalog_dir(temp_catalog_dir)

    # Create a node
    node_name = "test_node"
    node = Node.create(node_name)

    # Create a run associated with the node
    run_name = "test_run"
    run = node.create_run(run_name)

    # Check if the run was created
    assert Run.get(node_name, run_name) == run
