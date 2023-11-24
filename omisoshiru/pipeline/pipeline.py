import os
from dataclasses import dataclass
from typing import Callable, ClassVar, Dict, List, Optional, TypedDict, Union

import nbformat
from dataclass_wizard import YAMLWizard
from nbconvert.preprocessors import ClearOutputPreprocessor, ExecutePreprocessor


class InputDict(TypedDict):
    node: str
    run: str
    file: str


@dataclass
class Run:
    """
    Represents a run in the catalog.
    """

    node: str
    name: str
    inputs: Dict[str, InputDict]
    params: Dict[str, str]

    @classmethod
    def create(
        cls,
        node: str,
        name: str,
        inputs: Optional[Dict[str, InputDict]] = None,
        params: Optional[Dict[str, str]] = None,
        kernel_name: Optional[str] = None,
        timeout: Optional[int] = None,
    ) -> "Run":
        """
        Create a new run instance.

        Args:
            node (str): The name of the node.
            name (str): The name of the run.
            inputs (Optional[Dict[str, InputDict]]): Input information for the run.
            params (Optional[Dict[str, str]]): Parameters for the run.
            kernel_name (Optional[str]): The kernel name for execution.
            timeout (Optional[int]): Timeout for execution.

        Returns:
            Run: The created Run instance.
        """
        if cls.get(node, name):
            raise ValueError(f"Run name `{name}` already exists for node `{node}`.")

        inputs = inputs or {}
        params = params or {}

        run = cls(name=name, node=node, inputs=inputs, params=params)
        run.run(kernel_name=kernel_name, timeout=timeout)
        run.save()
        return run

    def save(self) -> None:
        """
        Save the run information to the catalog.
        """
        catalog = Catalog.load()
        catalog.runs.append(self)
        catalog.save()

    @classmethod
    def get(cls, node: str, name: str) -> Optional["Run"]:
        """
        Get a run instance by node and name.

        Args:
            node (str): The name of the node.
            name (str): The name of the run.

        Returns:
            Optional[Run]: The Run instance if found, else None.
        """
        catalog = Catalog.load()
        try:
            return next(
                filter(
                    lambda item: item.node == node and item.name == name, catalog.runs
                )
            )
        except StopIteration:
            return None

    @classmethod
    def search(cls, func: Optional[Callable] = None) -> List["Run"]:
        """
        Search for runs based on the provided filter function or expression.

        Args:
            func (Optional[Callable]): A filter function or expression to match runs.

        Returns:
            List[Run]: A list of matching Run instances.
        """
        runs = Catalog.load().runs
        if func is not None:
            runs = list(filter(func, runs))
        return runs

    def run(
        self, kernel_name: Optional[str] = None, timeout: Optional[int] = None
    ) -> None:
        """
        Execute the run.

        Args:
            kernel_name (Optional[str]): The kernel name for execution.
            timeout (Optional[int]): Timeout for execution.
        """
        os.makedirs(self.get_dir(), exist_ok=True)
        os.environ.update(
            **{
                f"PIPELINE_INPUT_{k}": os.path.join(
                    Run.get(v["node"], v["run"]).get_dir(), v["file"]
                )
                for k, v in self.inputs.items()
            }
        )
        os.environ.update(**{f"PIPELINE_PARAM_{k}": v for k, v in self.params.items()})

        with open(Node.get(self.node).get_path(), encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)

        ClearOutputPreprocessor().preprocess(nb, {})

        def handle_cell_start(cell, cell_index):
            max_length = 100
            source = repr(cell.get("source", ""))
            source = source[:max_length] + "..." if len(source) > max_length else source
            print(f"Executing cell {cell_index} | {source}")

        kernel_name = kernel_name or ""

        ep = ExecutePreprocessor(
            kernel_name=kernel_name,
            timeout=timeout,
            on_cell_start=handle_cell_start,
        )
        ep.preprocess(nb, {"metadata": {"path": self.get_dir()}})

        with open(
            os.path.join(self.get_dir(), f"{self.name}.ipynb"), "w", encoding="utf-8"
        ) as f:
            nbformat.write(nb, f)

    def get_dir(self) -> str:
        """
        Get the directory path for the run.

        Returns:
            str: The directory path.
        """
        return os.path.join(
            Catalog.get_catalog_dir(), "nodes", self.node, "runs", self.name
        )

    def get_files(self) -> List[str]:
        """
        Get the list of files in the run directory.

        Returns:
            List[str]: The list of files in the run directory
        """
        return os.listdir(self.get_dir())


@dataclass
class Node:
    """
    Represents a node in the catalog.
    """

    name: str

    @classmethod
    def create(cls, name: str) -> "Node":
        """
        Create a new node instance.

        Args:
            name (str): The name of the node.

        Returns:
            Node: The created Node instance.
        """
        if cls.get(name):
            raise ValueError(f"Node name `{name}` already exists.")

        node = cls(name=name)
        os.makedirs(os.path.dirname(node.get_path()), exist_ok=True)
        if not os.path.exists(node.get_path()):
            nb = nbformat.from_dict(
                {
                    "cells": [],
                    "metadata": {},
                    "nbformat": 4,
                    "nbformat_minor": 5,
                }
            )
            with open(node.get_path(), "w", encoding="utf-8") as f:
                nbformat.write(nb, f)

        node.save()
        return node

    def save(self) -> None:
        """
        Save the node information to the catalog.
        """
        catalog = Catalog.load()
        catalog.nodes.append(self)
        catalog.save()

    @classmethod
    def get(cls, name: str) -> Optional["Node"]:
        """
        Get a node instance by name.

        Args:
            name (str): The name of the node.

        Returns:
            Optional[Node]: The Node instance if found, else None.
        """
        catalog = Catalog.load()
        try:
            return next(filter(lambda item: item.name == name, catalog.nodes))
        except StopIteration:
            return None

    @classmethod
    def search(cls, func: Optional[Callable] = None) -> List["Node"]:
        """
        Search for nodes based on the provided filter function or expression.

        Args:
            func (Optional[Callable]): A filter function or expression to match nodes.

        Returns:
            List[Node]: A list of matching Node instances.
        """
        nodes = Catalog.load().nodes
        if func is not None:
            nodes = list(filter(func, nodes))
        return nodes

    def get_runs(self):
        """
        Get exist runs associated with this node.

        Returns:
            List[Run]: runs associated with this node.
        """
        return Run.search(lambda x: x.node == self.name)

    def create_run(self, *args, **kwargs) -> Run:
        """
        Create a run associated with this node.

        Returns:
            Run: The created Run instance.
        """
        run = Run.create(self.name, *args, **kwargs)
        return run

    def get_path(self) -> str:
        """
        Get the file path for the node.

        Returns:
            str: The file path.
        """
        return os.path.join(
            Catalog.get_catalog_dir(), "nodes", self.name, f"{self.name}.ipynb"
        )


@dataclass
class Catalog(YAMLWizard):
    """
    Represents the catalog containing nodes and runs.
    """

    CATALOG_DIR: ClassVar[str] = os.getcwd()
    CATALOG_NAME: ClassVar[str] = "catalog.yml"

    nodes: List[Node]
    runs: List[Run]

    @classmethod
    def set_catalog_dir(cls, catalog_dir: Optional[str] = None) -> None:
        """
        Set the catalog directory.

        Args:
            catalog_dir (Optional[str]): The directory path.

        Returns:
            None
        """
        cls.CATALOG_DIR = catalog_dir or os.getcwd()

    @classmethod
    def get_catalog_dir(cls) -> str:
        """
        Get the catalog directory.

        Returns:
            str: The directory path.
        """
        return cls.CATALOG_DIR

    @classmethod
    def load(cls) -> "Catalog":
        """
        Load the catalog from the YAML file.

        Returns:
            Catalog: The loaded Catalog instance.
        """
        if not os.path.exists(os.path.join(cls.CATALOG_DIR, cls.CATALOG_NAME)):
            catalog = Catalog(nodes=[], runs=[])
            return catalog
        else:
            catalog = cls.from_yaml_file(
                os.path.join(cls.CATALOG_DIR, cls.CATALOG_NAME)
            )
            return catalog

    def save(self) -> None:
        """
        Save the catalog to the YAML file.
        """
        self.to_yaml_file(os.path.join(self.CATALOG_DIR, self.CATALOG_NAME))
