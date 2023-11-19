# omisoshiru

`omisoshiru` is a Python package that provides utility functions for various tasks, including text processing and data analysis. It includes modules for tasks such as text unification, replacement, tokenization, and mathematical operations.

## Installation

```bash
pip install git+https://github.com/s-shibasaki/omisoshiru.git
```

## Package Structure

- `omisoshiru/text`: Contains modules related to text processing.
- `omisoshiru/math`: Includes modules related to mathematical operations.
- `omisoshiru/datetime`: Provides utilities for date and time operations.

## Text Processing

### FuzzyReplacer

The `FuzzyReplacer`` class is designed for replacing text based on a reference list. It can replace the specified text with the most similar item from the reference list.

```python
from omisoshiru.text import FuzzyReplacer

replacer = FuzzyReplacer(["apple", "banana", "orange"])
result = replacer.replace("appl")
print(result)  # Output: "apple"
```

### Other Modules
- `join_str`: Concatenates a list of strings using the specified separator.
- `replace_text_ranges`: Replaces specified text ranges in a string.
- `unify_hz`: Unifies character width in a string.
- `Wakachi`: Tokenizes Japanese text using MeCab.
- Many other modules are included.

## Mathematical Operations

### Cosine Similarity

The `omisoshiru/math` package includes a `cosine_similarity` function for calculating the cosine similarity of vectors.

```python
from omisoshiru.math import cosine_similarity
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])
result = cosine_similarity(a, b)
print(result)  # Output: array([0.95941195, 0.99614986])
```

## Date and Time Processing

The `omisoshiru/datetime` package provides utilities for date and time operations. For example, the `date_to_str` function converts a date to a string.

```python
from omisoshiru.datetime import date_to_str
from datetime import datetime

date = datetime(2023, 11, 1)
result = date_to_str(date)
print(result)  # Output: '20231101'
```

## Author
S. Shibasaki

## License
This project is licensed under the MIT License.
