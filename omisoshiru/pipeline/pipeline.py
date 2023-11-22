import os
from typing import Any, Dict, List, Optional, Tuple

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def get_pipeline_dir() -> str:
    """
    Get the pipeline directory path.

    Returns:
        str: The path to the pipeline directory.
    """
    return os.environ.get("PIPELINE_DIR") or os.path.abspath(os.getcwd())


class Run:
    def __init__(
        self,
        name: str,
        node: Any,
        inputs: dict,
        params: dict,
        kernel_name: str = "",
        timeout: Optional[int] = None,
    ):
        """
        Initialize a Run object.

        Parameters:
            name (str): The name of the run.
            node (Any): The associated Node object.
            inputs (dict): Input data for the run.
            params (dict): Parameters for the run.
            kernel_name (str, optional): The kernel name for notebook execution. Default is "".
            timeout (Optional[int], optional): The timeout for notebook execution. Default is None.
        """
        self.name = name
        self.node = node
        self.inputs = inputs
        self.params = params
        self.run(kernel_name, timeout)

    def run(self, kernel_name: str, timeout: Optional[int]):
        """
        Run the associated Node with the specified parameters.

        Parameters:
            kernel_name (str): The kernel name for notebook execution.
            timeout (Optional[int]): The timeout for notebook execution.
        """
        os.makedirs(self.get_dir(), exist_ok=True)

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

    def get_dir(self) -> str:
        """
        Get the directory path for the run.

        Returns:
            str: The path to the run directory.
        """
        return os.path.join(get_pipeline_dir(), "runs", self.name)


class Node:
    def __init__(
        self,
        name: str,
        inputs: List[str],
        outputs: List[str],
        params: List[str],
    ):
        """
        Initialize a Node object.

        Parameters:
            name (str): The name of the node.
            inputs (List[str]): Input names for the node.
            outputs (List[str]): Output names for the node.
            params (List[str]): Parameter names for the node.
        """
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
    ) -> Run:
        """
        Run the node with the specified parameters.

        Parameters:
            name (str): The name of the run.
            inputs (Dict[str, Tuple[Run, str]]): Input data for the run.
            params (Dict[str, str]): Parameters for the run.
            timeout (Optional[int], optional): The timeout for notebook execution. Default is None.
            kernel_name (Optional[str], optional): The kernel name for notebook execution. Default is "".

        Returns:
            Run: The Run object associated with the run.
        """
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

    def get_file(self) -> str:
        """
        Get the file path for the node.

        Returns:
            str: The path to the node file.
        """
        return os.path.join(
            get_pipeline_dir(), "nodes", self.name, self.name + ".ipynb"
        )


class Pipeline:
    def __init__(self):
        """
        Initialize a Pipeline object.
        """
        self.nodes = []

    def add_node(self, node: Node):
        """
        Add a Node to the pipeline.

        Parameters:
            node (Node): The Node object to add to the pipeline.
        """
        self.nodes.append(node)

    def get_runs(self) -> List[Run]:
        """
        Get a list of all runs in the pipeline.

        Returns:
            List[Run]: A list of Run objects in the pipeline.
        """
        return [run for node in self.nodes for run in node.runs]
