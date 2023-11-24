from torch.utils.data import IterableDataset


class DynamicDataset(IterableDataset):
    def __init__(self, data, epoch_processor=None):
        if epoch_processor is None:
            epoch_processor = lambda x: x
        elif not callable(epoch_processor):
            raise TypeError("epoch_processor must be callable")

        self.data = data
        self.epoch_processor = epoch_processor
        self.epoch = -1

    def __iter__(self):
        self.epoch += 1
        epoch_iterable = self.epoch_processor(self.epoch, self.data)
        return iter(epoch_iterable)
