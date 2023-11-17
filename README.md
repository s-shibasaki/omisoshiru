# omisoshiru: Data Analysis Utilities

`omisoshiru` is a Python library that provides a collection of common utilities for data analysis tasks. Whether you're cleaning, exploring, or visualizing your data, `omisoshiru` aims to simplify and streamline your workflow.

## Installation

You can install Your Library using pip:

```bash
pip install git+https://github.com/s-shibasaki/omisoshiru.git
```

## Usage

For example, to use the `WakachiReplacer` class, follow these steps:

```python
from omisoshiru.text import WakachiReplacer

replace_dict = {
    "りんご": "果物",
    "ばなな": "果物",
    "オレンジ": "果物",
    "車": "乗り物",
    "自転車": "乗り物",
    "犬": "動物",
    "猫": "動物",
}
replacer = WakachiReplacer(replace_dict)

text = "私はりんごが好きです。"
result = replacer.replace(text)
print(result)
# 私は果物が好きです。

text = "私は車を運転し、自転車に乗ります。犬と猫がいます。"
result = replacer.replace(text)
print(result)
# 私は乗り物を運転し、乗り物に乗ります。動物と動物が好きです。
```

## Documentation (Work in Progress)

Documentation for this project is currently under development.

If you have specific questions or need assistance, feel free to [open an issue](https://github.com/s-shibasaki/omisoshiru/issues).

## License

This project is licensed under the MIT License.
