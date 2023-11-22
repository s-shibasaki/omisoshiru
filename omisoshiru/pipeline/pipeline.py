import os
from typing import Any, Dict, List, Optional, Tuple

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def get_pipeline_dir():
    return os.environ.get("PIPELINE_DIR") or os.path.abspath(os.getcwd())


class Run:
    def __init__(
        self,
        name: str,
        node: Any,
        inputs: dict,
        params: dict,
        kernel_name="",
        timeout=None,
    ):
        self.name = name
        self.node = node
        self.inputs = inputs
        self.params = params

        self.run(kernel_name, timeout)

    def run(self, kernel_name, timeout):
        os.makedirs(self.get_dir(), exist_ok=True)

        # for src, dst in zip(self.inputs, self.node.inputs):
        #     os.symlink(os.path.abspath(src), os.path.join(self.name, dst))

        os.environ.update(
            **{
                "PIPELINE_INPUT_" + k: os.path.join(v[0].get_dir(), v[1])
                for k, v in self.inputs.items()
            }
        )
        os.environ.update(**{"PIPELINE_PARAM_" + k: v for k, v in self.params.items()})

        with open(self.node.get_file()) as f:
            nb = nbformat.read(f, as_version=4)

        ep = ExecutePreprocessor(kernel_name=kernel_name, timeout=timeout)
        ep.preprocess(nb, {"metadata": {"path": self.get_dir()}})

        with open(
            os.path.join(self.get_dir(), self.name + ".ipynb"), "w", encoding="utf-8"
        ) as f:
            nbformat.write(nb, f)

    def get_dir(self):
        return os.path.join(get_pipeline_dir(), "runs", self.name)


class Node:
    def __init__(
        self,
        name: str,
        inputs: List[str],
        outputs: List[str],
        params: List[str],
    ):
        self.name = name
        self.inputs = inputs
        self.outputs = outputs
        self.params = params
        self.runs = []

    def run(
        self,
        name: str,
        inputs: Dict[str, Tuple[Run, str]],
        params: Dict[str, str],
        timeout: Optional[int] = None,
        kernel_name: Optional[str] = "",
    ):
        run = Run(
            name=name,
            node=self,
            inputs=inputs,
            params=params,
            kernel_name=kernel_name,
            timeout=timeout,
        )
        self.runs.append(run)
        return run

    def get_file(self):
        return os.path.join(
            get_pipeline_dir(), "nodes", self.name, self.name + ".ipynb"
        )


class Pipeline:
    def __init__(self):
        self.nodes = []

    def add_node(self, node: Node):
        self.nodes.append(node)

    def get_runs(self):
        return [run for node in self.nodes for run in node.runs]
