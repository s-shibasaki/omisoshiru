"""
Pipeline Module

This module provides a simple pipeline framework for orchestrating and executing data processing tasks using Jupyter Notebooks.
"""


from .pipeline import Node, Pipeline, Run

__all__ = ["Node", "Run", "Pipeline"]
