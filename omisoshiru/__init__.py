"""
omisoshiru: A Python Package for Text Processing and Data Analysis

`omisoshiru` is a Python package that provides utility functions for various tasks, including text processing and data analysis. It includes modules for tasks such as text unification, replacement, tokenization, and mathematical operations.

Package Structure:
- omisoshiru/text: Contains modules related to text processing.
- omisoshiru/math: Includes modules related to mathematical operations.
- omisoshiru/datetime: Provides utilities for date and time operations.

Text Processing Modules:
- FuzzyReplacer: Replaces text based on a reference list using fuzzy matching.
- join_str: Concatenates a list of strings using the specified separator.
- replace_text_ranges: Replaces specified text ranges in a string.
- unify_hz: Unifies character width in a string.
- Wakachi: Tokenizes Japanese text using MeCab.
- Many other modules for various text processing tasks.

Mathematical Operations:
- cosine_similarity: Calculates the cosine similarity of vectors.

Date and Time Processing:
- date_to_str: Converts a date to a string.

Usage:
```python
# Example of using FuzzyReplacer
from omisoshiru.text import FuzzyReplacer

replacer = FuzzyReplacer(["apple", "banana", "orange"])
result = replacer.replace("appl")
print(result)  # Output: "apple"
```

For more details and examples, refer to the documentation.

Author: S. Shibasaki
License: MIT License
"""
