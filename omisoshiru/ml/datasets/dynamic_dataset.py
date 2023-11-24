from torch.utils.data import IterableDataset


class DynamicDataset(IterableDataset):
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
