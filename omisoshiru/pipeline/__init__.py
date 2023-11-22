"""
Pipeline Module

This module provides a simple pipeline framework for orchestrating and executing data processing tasks using Jupyter Notebooks.

Classes:
- Node: Represents a processing step in the pipeline.
- Run: Represents the execution of a Node with specified inputs and parameters.
- Pipeline: Represents a collection of Nodes organized in a sequential pipeline.

Usage:
1. Define Nodes with input and output specifications.
2. Create a Pipeline and add Nodes to it.
3. Execute Runs within the Pipeline to process data through the defined Nodes.

Example:
```python
from omisoshiru.pipeline import Node, Pipeline

# Define Nodes
node1 = Node(name="node1", inputs=["input1"], outputs=["output1"], params=["param1"])
node2 = Node(name="node2", inputs=["input1"], outputs=["output2"], params=["param2"])

# Create Pipeline and add Nodes
pipeline = Pipeline()
pipeline.add_node(node1)
pipeline.add_node(node2)

# Execute Runs in the Pipeline
run1 = node1.run(name="run1", inputs={"input1": (input_data, "data.csv")}, params={"param1": "value1"})
run2 = node2.run(name="run2", inputs={"input1": (run1, "output1")}, params={"param2": "value2"})
```
Note: Ensure that the 'PIPELINE_DIR' environment variable is set to the desired base directory for storing pipeline-related files.
"""


from .pipeline import Node, Pipeline, Run

__all__ = ["Node", "Run", "Pipeline"]
