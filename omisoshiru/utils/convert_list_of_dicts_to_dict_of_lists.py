from typing import Literal, Optional

import numpy as np
import torch


def convert_list_of_dicts_to_dict_of_lists(
    list_of_dicts, nest=None, stack: Optional[Literal["numpy", "torch"]] = None
):
    keys, values = zip(*[zip(*i.items()) for i in list_of_dicts])
    dict_of_lists = {k: v for k, v in zip(keys[0], zip(*values))}

    if isinstance(nest, int) and nest > 1:
        dict_of_lists = {
            k: convert_list_of_dicts_to_dict_of_lists(v, nest - 1, stack)
            for k, v in dict_of_lists.items()
        }
    elif stack == "numpy":
        dict_of_lists = {k: np.stack(v) for k, v in dict_of_lists.items()}
    elif stack == "torch":
        print("STACKING")
        dict_of_lists = {k: torch.stack(v) for k, v in dict_of_lists.items()}

    return dict_of_lists
