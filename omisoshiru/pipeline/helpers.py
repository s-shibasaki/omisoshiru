import os
import warnings
from typing import List, Optional, Tuple

from .pipeline import Catalog, Node, Run


class NotebookHelper:
    def __init__(self):
        self._run = None
        self._node = None
        self._set_attribute(os.getcwd())
        self._obtain_args()
        print("Node:", self._node)
        print("Run:", self._run)
        for k, v in self._inputs.items():
            print(f"Input {k}: {v}")
        for k, v in self._params.items():
            print(f"Param {k}: {v}")

    def _obtain_args(self):
        self._inputs = {
            k.replace("PIPELINE_INPUT_", "").lower(): v
            for k, v in os.environ.items()
            if k.startswith("PIPELINE_INPUT_")
        }
        self._params = {
            k.replace("PIPELINE_PARAM_", "").lower(): v
            for k, v in os.environ.items()
            if k.startswith("PIPELINE_PARAM_")
        }

    def _set_attribute(self, cwd):
        remaining, name = os.path.split(cwd)
        remaining, typ = os.path.split(remaining)
        if typ == "nodes":
            self._node = name
            Catalog.set_catalog_dir(remaining)
        elif typ == "runs":
            self._run = name
            self._set_attribute(remaining)

    def get_current_run(self):
        return Run.get(self._run) if self._run else None

    def get_current_node(self):
        return Node.get(self._node) if self._node else None

    def get_input(self, name, default_value=None):
        name = name.lower()
        value = self._inputs.get(name)
        if value is None:
            warnings.warn(
                f"Input `{name}` not found in environment variables. Using default value: {default_value}"
            )
            value = default_value
        return value

    def get_param(self, name, default_value=None):
        name = name.lower()
        value = self._params.get(name)
        if value is None:
            warnings.warn(
                f"Param `{name}` not found in environment variables. Using default value: {default_value}"
            )
            value = default_value
        return value
