import os
import shutil
import tempfile

import nbformat
import pytest

from omisoshiru.pipeline import Node, Pipeline, Run


@pytest.fixture
def temporary_directory(request):
    temp_dir = tempfile.mkdtemp()
    os.environ.update(PIPELINE_DIR=temp_dir)
    from omisoshiru.pipeline import Node, Pipeline, Run

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


def test_pipeline_creation():
    pipeline = Pipeline()
    assert pipeline.nodes == []


def test_add_node():
    pipeline = Pipeline()
    pipeline.add_node(Node("node1", ["input1"], ["output1"], ["param1"]))
    assert len(pipeline.nodes) == 1
    assert isinstance(pipeline.nodes[0], Node)


@pytest.mark.slow
def test_get_runs(temporary_directory):
    pipeline = Pipeline()
    node = Node("node1", ["input1"], ["output1"], ["param1"])
    run = node.run("run1", {}, {}, timeout=60)
    pipeline.add_node(node)

    runs = pipeline.get_runs()
    assert len(runs) == 1
    assert runs[0] is run
