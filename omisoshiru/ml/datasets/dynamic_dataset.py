from torch.utils.data import IterableDataset


class DynamicDataset(IterableDataset):
    """
    A PyTorch IterableDataset implementation for handling dynamic and iterable datasets.

    This dataset allows for dynamic initialization through the provided `initialize_function`, enabling flexibility
    in data loading strategies. It is designed to be used with PyTorch's DataLoader for efficient and flexible
    data loading during training or evaluation.

    Parameters:
    - data (iterable): The raw data that the dataset will iterate over.
    - initialize_function (callable, optional): A function used for dynamic initialization of the dataset. If None,
      the dataset will default to a simple identity initialization function. The function should take the raw data
      as input and return the data to be used for the current epoch.

    Example:
    ```python
    # Example usage with DataLoader
    data = [1, 2, 3, 4, 5]
    initialize_function = lambda x: x[::-1]  # Reverses the data for each epoch
    dynamic_dataset = DynamicDataset(data, initialize_function)

    dataloader = DataLoader(dynamic_dataset, batch_size=2, num_workers=2)
    for batch in dataloader:
        # Training or evaluation logic with the batch
    ```

    Note:
    - The `initialize_function` should be a callable that takes the raw data and returns the data for the current epoch.
      It allows for dynamic changes to the dataset between epochs.
    - This dataset is intended to be used with PyTorch's DataLoader, which handles the iteration and parallelization
      aspects efficiently.

    References:
    - PyTorch IterableDataset: https://pytorch.org/docs/stable/data.html#torch.utils.data.IterableDataset
    """

    def __init__(self, data, initialize_function=None):
        if initialize_function is None:
            initialize_function = lambda x: x
        elif not callable(initialize_function):
            raise TypeError("initialize_function must be callable")

        self.data = data
        self.initialize_function = initialize_function

    def __iter__(self):
        epoch_data = self.initialize_function(self.data)
        self.epoch_iterator = iter(epoch_data)
        return self

    def __next__(self):
        return next(self.epoch_iterator)
