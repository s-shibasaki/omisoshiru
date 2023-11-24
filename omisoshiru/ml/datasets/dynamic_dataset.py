from torch.utils.data import IterableDataset


class DynamicDataset(IterableDataset):
    def __init__(self, data, epoch_processor=None):
        if epoch_processor is None:
            epoch_processor = lambda x: x
        elif not callable(epoch_processor):
            raise TypeError("epoch_processor must be callable")

        self.data = data
        self.epoch_processor = epoch_processor
        self.epoch = 0

    def __iter__(self):
        self.epoch_iterable = self.epoch_processor(self.epoch, self.data)
        return self

    def __next__(self):
        try:
            return next(self.epoch_iterable)
        except StopIteration:
            self.epoch += 1
            raise StopIteration
