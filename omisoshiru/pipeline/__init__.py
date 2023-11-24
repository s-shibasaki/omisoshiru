"""
Pipeline Module

This module provides a simple pipeline framework for orchestrating and executing data processing tasks using Jupyter Notebooks.
"""


from .notebook_helper import NotebookHelper
from .pipeline import Node, Pipeline, Run, get_catalog_dir, set_catalog_dir

__all__ = [
    "Node",
    "Run",
    "Pipeline",
    "NotebookHelper",
    "set_catalog_dir",
    "get_catalog_dir",
]
