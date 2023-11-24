import pytest

from omisoshiru.ml.datasets import DynamicDataset


def test_dynamic_dataset_init():
    data = [1, 2, 3]
    initialize_function = lambda x: x
    dataset = DynamicDataset(data, initialize_function)
    assert dataset.data == data
    assert dataset.initialize_function == initialize_function


def test_dynamic_dataset_init_with_none():
    data = []
    initialize_function = lambda x: x
    dataset = DynamicDataset(data, initialize_function)
    assert dataset.data == []
    assert dataset.initialize_function == initialize_function


def test_dynamic_dataset_init_with_generator():
    data = (x for x in range(3))
    initialize_function = lambda x: x
    dataset = DynamicDataset(data, initialize_function)
    assert list(dataset.data) == list(range(3))
    assert dataset.initialize_function == initialize_function


def test_dynamic_dataset_init_with_generator_function():
    data = range(3)
    initialize_function = lambda x: x
    dataset = DynamicDataset(data, initialize_function)
    assert list(dataset.data) == list(range(3))
    assert dataset.initialize_function == initialize_function


def test_dynamic_dataset_init_with_non_callable_init_function():
    data = [1, 2, 3]
    initialize_function = 123
    with pytest.raises(TypeError):
        DynamicDataset(data, initialize_function)


def test_dynamic_dataset_init_with_callable_init_function():
    data = [1, 2, 3]
    initialize_function = lambda x: x
    dataset = DynamicDataset(data, initialize_function)
    assert dataset.data == data
    assert dataset.initialize_function == initialize_function


def test_dynamic_dataset_iter():
    data = [1, 2, 3]
    initialize_function = lambda x: x
    dataset = DynamicDataset(data, initialize_function)
    assert list(dataset) == data


def test_dynamic_dataset_next():
    data = [1, 2, 3]
    initialize_function = lambda x: x
    dataset = DynamicDataset(data, initialize_function)
    it = iter(dataset)
    assert next(it) == 1
    assert next(it) == 2
    assert next(it) == 3
    with pytest.raises(StopIteration):
        next(it)
