"""
omisoshiru: A collection of utility modules for various tasks.

This package provides a set of utility modules for tasks such as text processing, graph algorithms, date-time operations, mathematical calculations, and more.

Available submodules:
    - algorithm: Algorithms and utility functions.
    - collections: Custom data structures and collection-related utilities.
    - datetime: Date and time manipulation functions.
    - graph: Graph-related algorithms and utilities.
    - math: Mathematical functions and calculations.
    - text: Text processing utilities.

Examples:
    1. Text Processing:
        >>> from omisoshiru.text.wakachi import Wakachi, WakachiMatcher, WakachiReplacer
        >>> wakachi = Wakachi(allow_whitespace=True)
        >>> input_text = "これはテストです。"
        >>> tokens = wakachi.parse(input_text)
        >>> print(tokens)
        ['これ', 'は', 'テスト', 'です', '。']

        >>> wakachi_matcher = WakachiMatcher()
        >>> pattern_list = ["桜の花"]
        >>> matches = wakachi_matcher.match(pattern_list, input_text)
        >>> print(matches)
        [((0, 3), "桜の花"), ((18, 21), "桜の花")]

        >>> wakachi_replacer = WakachiReplacer({"りんご": "フルーツ", "ばなな": "フルーツ"})
        >>> replaced_text = wakachi_replacer.replace("りんごとばななが好きです。")
        >>> print(replaced_text)
        "フルーツとフルーツが好きです。"

        >>> from omisoshiru.text.fuzzy_replacer import FuzzyReplacer
        >>> fuzzy_replacer = FuzzyReplacer(["apple", "orange", "banana"])
        >>> replaced_fuzzy = fuzzy_replacer.replace("applle")
        >>> print(replaced_fuzzy)
        "apple"

    2. Graph Algorithms:
        >>> import networkx as nx
        >>> from omisoshiru.graph import bfs_select_nodes
        >>> # Create a simple undirected graph
        >>> graph = nx.Graph()
        >>> graph.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 5), (4, 5)])
        >>> selected_nodes = bfs_select_nodes(graph, start_node=1, target_count=3)
        >>> print(selected_nodes)
        [1, 2, 3]


    3. Date-Time Operations:
        >>> from omisoshiru.datetime import date_to_str
        >>> from datetime import datetime
        >>> date_obj = datetime(2023, 1, 1)
        >>> formatted_date = date_to_str(date_obj)
        >>> print(formatted_date)
        '20230101'

    4. Mathematical Calculations:
        >>> from omisoshiru.math import cosine_similarity
        >>> import numpy as np
        >>> a = np.array([[1, 2, 3], [4, 5, 6]])
        >>> b = np.array([[7, 8, 9], [10, 11, 12]])
        >>> similarity_values = cosine_similarity(a, b)
        >>> print(similarity_values)
        array([0.95941195, 0.99614986])

    5. Collection Utilities:
        >>> from omisoshiru.collections import PriorityQueue
        >>> pq = PriorityQueue()
        >>> pq.push(3, priority=2)
        >>> pq.push(1, priority=1)
        >>> pq.push(2, priority=3)
        >>> popped_item = pq.pop()
        >>> print(popped_item)
        (1, 1)
"""
from . import algorithm, collections, datetime, graph, math, text
