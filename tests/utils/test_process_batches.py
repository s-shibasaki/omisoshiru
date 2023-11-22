import numpy as np
import pandas as pd
import pytest
import torch

from omisoshiru.utils import process_batches


# Test case 1: Test with a NumPy array, batch size = 2, result_type = "numpy"
def test_process_batches_numpy_array():
    data = np.array([1, 2, 3, 4, 5, 6])
    result = process_batches(data, lambda x: x * 2, batch_size=2, result_type="numpy")
    expected_result = np.array([2, 4, 6, 8, 10, 12])
    assert np.array_equal(result, expected_result)


# Test case 2: Test with a pandas DataFrame, batch size = 2, result_type = "numpy"
def test_process_batches_pandas_dataframe():
    data = pd.DataFrame({"col": [1, 2, 3, 4, 5, 6]})
    result = process_batches(
        data, lambda x: x.col.values * 2, batch_size=2, result_type="numpy"
    )
    expected_result = np.array([2, 4, 6, 8, 10, 12])
    assert np.array_equal(result, expected_result)


# Test case 3: Test with a torch tensor, batch size = 2, result_type = "torch"
def test_process_batches_torch_tensor():
    data = torch.tensor([1, 2, 3, 4, 5, 6])
    result = process_batches(data, lambda x: x * 2, batch_size=2, result_type="torch")
    expected_result = torch.tensor([2, 4, 6, 8, 10, 12])
    assert torch.equal(result, expected_result)


# Test case 4: Test with an empty iterable, batch size = 2, result_type = None
def test_process_batches_empty_iterable():
    data = np.array([])
    result = process_batches(data, lambda x: x * 2, batch_size=2)
    expected_result = []
    assert result == expected_result


# Test case 5: Test with a large batch size, result_type = "numpy"
def test_process_batches_large_batch_size():
    data = np.array([1, 2, 3, 4, 5, 6])
    result = process_batches(data, lambda x: x * 2, batch_size=10, result_type="numpy")
    expected_result = np.array([2, 4, 6, 8, 10, 12])
    assert np.array_equal(result, expected_result)


# Test case 6: Test with a batch size larger than the length of the iterable, result_type = None
def test_process_batches_large_batch_size_iterable_length():
    data = np.array([1, 2, 3, 4, 5, 6])
    result = process_batches(data, lambda x: x * 2, batch_size=20)
    expected_result = [np.array([2, 4, 6, 8, 10, 12])]
    assert all(
        [
            np.array_equal(res_item, exp_item)
            for res_item, exp_item in zip(result, expected_result)
        ]
    )
