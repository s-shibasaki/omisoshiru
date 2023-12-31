from typing import Callable, Literal, Optional, Union

import numpy as np
import pandas as pd
import torch
from tqdm.auto import tqdm

from .convert_dict_of_lists_to_list_of_dicts import (
    convert_dict_of_lists_to_list_of_dicts,
)
from .convert_list_of_dicts_to_dict_of_lists import (
    convert_list_of_dicts_to_dict_of_lists,
)


def process_batches(
    iterable: Union[pd.DataFrame, pd.Series, list, np.ndarray, torch.Tensor],
    function: Callable,
    batch_size: int,
    result_type: Optional[Literal["numpy", "torch"]] = None,
    axis: Optional[int] = None,
    dictionary_input: Optional[Union[Literal["numpy", "torch"], bool]] = None,
) -> Union[np.ndarray, torch.Tensor, list]:
    """
    Process data in batches using a specified function.

    Parameters:
        iterable (Union[pd.DataFrame, pd.Series, list, np.ndarray, torch.Tensor]):
            The input data to be processed in batches.
        function (Callable):
            The function to be applied to each batch.
        batch_size (int):
            The size of each batch.
        result_type (Optional[Literal["numpy", "torch"]], optional):
            The desired type of the result.
            If "numpy", the result will be a NumPy array.
            If "torch", the result will be a PyTorch tensor.
            If None, the result will be a list. Default is None.
        axis (Optional[int], optional):
            The axis along which to concatenate the batches for NumPy or PyTorch results.
            Applicable only if result_type is "numpy" or "torch". Default is None.

    Returns:
        Union[np.ndarray, torch.Tensor, list]:
            The result of applying the function to the batches.
            The type of the result depends on the value of result_type.
            If result_type is "numpy", the result is a NumPy array.
            If result_type is "torch", the result is a PyTorch tensor.
            If result_type is None, the result is a list.

    Example:
        >>> data = np.array([1, 2, 3, 4, 5, 6])
        >>> result = process_batches(data, lambda x: x * 2, batch_size=2, result_type="numpy")
        >>> print(result)
        array([2, 4, 6, 8, 10, 12])
    """
    if dictionary_input:
        iterable = convert_dict_of_lists_to_list_of_dicts(iterable)

    length = len(iterable)

    # If iterable is a DataFrame or Series, use iloc for slicing
    if isinstance(iterable, (pd.DataFrame, pd.Series)):
        iterable = iterable.iloc

    # Create batches
    batches = [
        iterable[i : min(i + batch_size, length)] for i in range(0, length, batch_size)
    ]

    # Apply the function to each batch
    results = []
    for batch in tqdm(batches):
        if dictionary_input == "numpy":
            batch = convert_list_of_dicts_to_dict_of_lists(batch, stack="numpy")
        elif dictionary_input == "torch":
            batch = convert_list_of_dicts_to_dict_of_lists(batch, stack="torch")
        elif dictionary_input:
            batch = convert_list_of_dicts_to_dict_of_lists(batch)
        results.append(function(batch))

    # Concatenate batches based on result_type
    if result_type == "numpy":
        results = np.concatenate(results, axis=axis)
    elif result_type == "torch":
        results = torch.cat(results, dim=axis)
    elif result_type == "list":
        results = [sample for batch in results for sample in batch]

    return results
