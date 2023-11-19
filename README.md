# omisoshiru

[![Under Development](https://img.shields.io/badge/status-under%20development-orange)](https://shields.io/)
![Build Status](https://github.com/s-shibasaki/omisoshiru/actions/workflows/test.yml/badge.svg)


**omisoshiru** is a collection of utility modules for various tasks. It provides a set of submodules for tasks such as text processing, graph algorithms, date-time operations, mathematical calculations, and more.

## Modules

1. **algorithm**: Algorithms and utility functions.
2. **collections**: Custom data structures and collection-related utilities.
3. **datetime**: Date and time manipulation functions.
4. **graph**: Graph-related algorithms and utilities.
5. **math**: Mathematical functions and calculations.
6. **text**: Text processing utilities.

## Examples

### Text Processing

```python
from omisoshiru.text.wakachi import Wakachi, WakachiMatcher, WakachiReplacer
wakachi = Wakachi(allow_whitespace=True)
input_text = "これはテストです。"
tokens = wakachi.parse(input_text)
print(tokens)

wakachi_matcher = WakachiMatcher()
pattern_list = ["桜の花"]
matches = wakachi_matcher.match(pattern_list, input_text)
print(matches)

wakachi_replacer = WakachiReplacer({"りんご": "フルーツ", "ばなな": "フルーツ"})
replaced_text = wakachi_replacer.replace("りんごとばななが好きです。")
print(replaced_text)
```

### Graph Algorithms

```python
import networkx as nx
from omisoshiru.graph import bfs_select_nodes

# Create a simple undirected graph
graph = nx.Graph()
graph.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 5), (4, 5)])

# Perform BFS to select a specified number of nodes
selected_nodes = bfs_select_nodes(graph, start_node=1, target_count=3)
print(selected_nodes)
```

### Date-Time Operations

```python
from omisoshiru.datetime import date_to_str
from datetime import datetime
date_obj = datetime(2023, 1, 1)
formatted_date = date_to_str(date_obj)
print(formatted_date)
```

### Mathematical Calculations

```python
from omisoshiru.math import cosine_similarity
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])
similarity_values = cosine_similarity(a, b)
print(similarity_values)
```

### Collection Utilities

```python
from omisoshiru.collections import PriorityQueue
pq = PriorityQueue()
pq.push(3, priority=2)
pq.push(1, priority=1)
pq.push(2, priority=3)
popped_item = pq.pop()
print(popped_item)
```

## Installation

```bash
pip install git+https://github.com/s-shibasaki/omisoshiru.git
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
