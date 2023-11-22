from typing import Callable, Literal, Optional, Union

import numpy as np
import pandas as pd
import torch


def process_batches(
    iterable: Union[pd.DataFrame, pd.Series, list, np.ndarray, torch.Tensor],
    function: Callable,
    batch_size: int,
    result_type: Optional[Literal["numpy", "torch"]] = None,
    axis: Optional[int] = None,
) -> Union[np.ndarray, torch.Tensor, list]:
    length = len(iterable)
    if isinstance(iterable, (pd.DataFrame, pd.Series)):
        iterable = iterable.iloc
    batches = [
        iterable[i : min(i + batch_size, length)]
        for i in range(0, len(iterable), batch_size)
    ]
    results = [function(batch) for batch in batches]

    if result_type == "numpy":
        results = np.concatenate(results, axis=axis)
    elif result_type == "torch":
        results = torch.cat(results, dim=axis)

    return results
