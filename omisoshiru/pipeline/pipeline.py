import os
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

import nbformat
from dataclass_wizard import YAMLWizard
from nbconvert.preprocessors import ExecutePreprocessor


@dataclass
class Run:
    node: str
    name: str
    inputs: dict
    params: dict

    @classmethod
    def create(cls, node, name, inputs, params, kernel_name, timeout):
        if cls.get(node, name):
            raise ValueError(f"Run name `{name}` is already existed for node `{node}`.")

        # instantiate
        run = cls(name=name, node=node, inputs=inputs, params=params)

        # run
        run.run(kernel_name=kernel_name, timeout=timeout)

        # add to catalog
        run.save()

        # return instance
        return run

    def save(self):
        catalog = Catalog.load()
        catalog.runs.append(self)
        catalog.save()

    @classmethod
    def get(cls, node, name):
        return Catalog.load().get_run(node, name)

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
                "PIPELINE_INPUT_"
                + k: os.path.join(Run.get(run_name).get_dir(), "input_name")
                for k, (run_name, input_name) in self.inputs.items()
            }
        )
        os.environ.update(**{"PIPELINE_PARAM_" + k: v for k, v in self.params.items()})

        with open(Node.get(self.node).get_file()) as f:
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
        return os.path.join(Catalog.get_pipeline_dir(), "runs", self.name)


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
            raise ValueError(f"Node name `{name}` is already existed.")

        # instantiate node
        node = cls(name=name, inputs=inputs, outputs=outputs, params=params)

        # create notebook
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

        # add to catalog
        node.save()

        # return instance
        return node

    def save(self):
        catalog = Catalog.load()
        catalog.nodes.append(self)
        catalog.save()

    @classmethod
    def get(self, name):
        return Catalog.load().get_node(name)

    def run(
        self,
        name: str,
        inputs: Dict[str, Tuple[str, str]],
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
        """
        Get the file path for the node.

        Returns:
            str: The path to the node file.
        """
        return os.path.join(
            Catalog.get_pipeline_dir(), "nodes", self.name, self.name + ".ipynb"
        )


@dataclass
class Catalog(YAMLWizard):
    CATALOG_DIR = os.getcwd()
    CATALOG_NAME = "catalog.yml"

    nodes: List[Node]
    runs: List[Run]

    @classmethod
    def set_catalog_dir(cls, catalog_dir=None):
        catalog_dir = catalog_dir or os.getcwd()
        cls.CATALOG_DIR = catalog_dir

    @classmethod
    def get_catalog_dir(cls) -> str:
        """
        Get the catalog directory path.

        Returns:
            str: The path to the catalog directory.
        """
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
