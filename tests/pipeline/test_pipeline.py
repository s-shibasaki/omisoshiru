import os
import shutil
import tempfile

import nbformat
import pytest

from omisoshiru.pipeline import Catalog, Node, Run


@pytest.fixture
def temporary_directory(request):
    temp_dir = tempfile.mkdtemp()
    Catalog.set_pipeline_dir(temp_dir)

    os.makedirs(os.path.join(temp_dir, "nodes", "node1"), exist_ok=True)
    with open(
        os.path.join(temp_dir, "nodes", "node1", "node1.ipynb"), "w", encoding="utf-8"
    ) as f:
        nbformat.write(
            nbformat.from_dict(
                {"cells": [], "metadata": {}, "nbformat": 4, "nbformat_minor": 5}
            ),
            f,
        )

    def cleanup():
        shutil.rmtree(temp_dir)

    request.addfinalizer(cleanup)
    return temp_dir


def test_node_creation():
    inputs = ["input1", "input2"]
    outputs = ["output1", "output2"]
    params = ["param1", "param2"]
    node = Node("name", inputs, outputs, params)
    assert node.name == "name"
    assert node.inputs == inputs
    assert node.outputs == outputs
    assert node.params == params
    assert node.runs == []


@pytest.mark.slow
def test_run_creation(temporary_directory):
    inputs = {
        "input1": (
            Run("run1", Node("node1", ["input1"], ["output1"], ["param1"]), {}, {}),
            "file1",
        )
    }
    params = {"param1": "value1"}
    node = Node("node1", ["input1"], ["output1"], ["param1"])
    run = node.run("run1", inputs, params, timeout=60)

    assert run.name == "run1"
    assert run.node == node
    assert run.inputs == inputs
    assert run.params == params


@pytest.mark.slow
def test_run_directory(temporary_directory):
    node = Node("node1", ["input1"], ["output1"], ["param1"])
    run = Run("run1", node, {}, {})
    run_dir = run.get_dir()
    expected_dir = os.path.join(temporary_directory, "runs", "run1")

    assert run_dir == expected_dir
    assert os.path.exists(run_dir)
