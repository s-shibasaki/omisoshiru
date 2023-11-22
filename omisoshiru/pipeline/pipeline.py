"""
Pipeline Module

This module provides a simple pipeline framework for orchestrating and executing data processing tasks using Jupyter Notebooks.

Classes:
- Run: Dataclass representing a pipeline run with methods for creation, execution, and retrieval.
- Node: Dataclass representing a processing node in the pipeline with methods for creation, execution, and file management.
- Catalog: Dataclass representing the catalog of nodes and runs with methods for loading, saving, and retrieval.

Note: This module assumes a directory structure where nodes and runs are organized within a catalog directory.

Usage:
1. Create nodes using the Node class, specifying input, output, and parameter names.
2. Create pipeline runs using the Run class, associating them with specific nodes, input data, and parameters.
3. Catalog keeps track of nodes and runs, allowing retrieval and persistence.

Example:
```python
# Create a node
node = Node.create(name="ProcessData", inputs=["input_data.csv"], outputs=["output_data.csv"], params=["param1", "param2"])

# Create a run for the node
run = node.run(name="Run1", inputs={"input_data.csv": {"node": "Source", "run": "Run1", "data": "source_data.csv"}}, params={"param1": "value1", "param2": "value2"}, kernel_name="python3", timeout=600)
```
"""

import os
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple, TypedDict

import nbformat
from dataclass_wizard import YAMLWizard
from nbconvert.preprocessors import ExecutePreprocessor


class InputDict(TypedDict):
    node: str
    run: str
    data: str


@dataclass
class Run:
    node: str
    name: str
    inputs: Dict[str, InputDict]
    params: Dict[str, str]

    @classmethod
    def create(cls, node, name, inputs, params, kernel_name, timeout):
        if cls.get(node, name):
            raise ValueError(f"Run name `{name}` already exists for node `{node}`.")

        run = cls(name=name, node=node, inputs=inputs, params=params)
        run.run(kernel_name=kernel_name, timeout=timeout)
        run.save()
        return run

    def save(self):
        catalog = Catalog.load()
        catalog.runs.append(self)
        catalog.save()

    @classmethod
    def get(cls, node, name):
        return Catalog.load().get_run(node, name)

    def run(self, kernel_name: str, timeout: Optional[int]):
        os.makedirs(self.get_dir(), exist_ok=True)
        os.environ.update(
            **{
                f"PIPELINE_INPUT_{k}": os.path.join(
                    Run.get(v["node"], v["run"]).get_dir(), v["data"]
                )
                for k, v in self.inputs.items()
            }
        )
        os.environ.update(**{f"PIPELINE_PARAM_{k}": v for k, v in self.params.items()})

        with open(Node.get(self.node).get_file()) as f:
            nb = nbformat.read(f, as_version=4)

        ep = ExecutePreprocessor(kernel_name=kernel_name, timeout=timeout)
        ep.preprocess(nb, {"metadata": {"path": self.get_dir()}})

        with open(
            os.path.join(self.get_dir(), f"{self.name}.ipynb"), "w", encoding="utf-8"
        ) as f:
            nbformat.write(nb, f)

    def get_dir(self) -> str:
        return os.path.join(Catalog.get_catalog_dir(), "runs", self.name)


@dataclass
class Node:
    name: str
    inputs: List[str]
    outputs: List[str]
    params: List[str]

    @classmethod
    def create(
        cls,
        name: str,
        inputs: List[str],
        outputs: List[str],
        params: List[str],
    ):
        if cls.get(name):
            raise ValueError(f"Node name `{name}` already exists.")

        node = cls(name=name, inputs=inputs, outputs=outputs, params=params)
        os.makedirs(os.path.dirname(node.get_file()), exist_ok=True)
        if not os.path.exists(node.get_file()):
            nb = nbformat.from_dict(
                {
                    "cells": [],
                    "metadata": {},
                    "nbformat": 4,
                    "nbformat_minor": 5,
                }
            )
            with open(node.get_file(), "w", encoding="utf-8") as f:
                nbformat.write(nb, f)

        node.save()
        return node

    def save(self):
        catalog = Catalog.load()
        catalog.nodes.append(self)
        catalog.save()

    @classmethod
    def get(cls, name):
        return Catalog.load().get_node(name)

    def run(
        self,
        name: str,
        inputs: Dict[str, InputDict],
        params: Dict[str, str],
        timeout: Optional[int] = None,
        kernel_name: Optional[str] = "",
    ) -> Run:
        run = Run.create(
            node=self.name,
            name=name,
            inputs=inputs,
            params=params,
            kernel_name=kernel_name,
            timeout=timeout,
        )
        return run

    def get_file(self) -> str:
        return os.path.join(
            Catalog.get_catalog_dir(), "nodes", self.name, f"{self.name}.ipynb"
        )


@dataclass
class Catalog(YAMLWizard):
    CATALOG_DIR = os.getcwd()
    CATALOG_NAME = "catalog.yml"

    nodes: List[Node]
    runs: List[Run]

    @classmethod
    def set_catalog_dir(cls, catalog_dir=None):
        cls.CATALOG_DIR = catalog_dir or os.getcwd()

    @classmethod
    def get_catalog_dir(cls) -> str:
        return cls.CATALOG_DIR

    @classmethod
    def load(cls):
        if not os.path.exists(os.path.join(cls.CATALOG_DIR, cls.CATALOG_NAME)):
            catalog = Catalog(nodes=[], runs=[])
            return catalog
        else:
            catalog = cls.from_yaml_file(
                os.path.join(cls.CATALOG_DIR, cls.CATALOG_NAME)
            )
            return catalog

    def save(self):
        self.to_yaml_file(os.path.join(self.CATALOG_DIR, self.CATALOG_NAME))

    def get_node(self, name):
        try:
            return next(filter(lambda item: item.name == name, self.nodes))
        except StopIteration:
            return None

    def get_run(self, node, name):
        try:
            return next(
                filter(lambda item: item.node == node and item.name == name, self.runs)
            )
        except StopIteration:
            return None
