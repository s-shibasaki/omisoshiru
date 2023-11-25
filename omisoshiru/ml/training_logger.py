import numpy as np
import pandas as pd


class TrainingLogger:
    def __init__(self):
        self.epoch = -1
        self.train_step_log = []
        self.eval_step_log = []
        self.epoch_log = []

    def epoch_init(self):
        self.epoch += 1

    def train_step(self, train_loss):
        self.train_step_log.append({"epoch": self.epoch, "train_loss": train_loss})

    def eval_step(self, eval_loss):
        self.eval_step_log.append({"epoch": self.epoch, "eval_loss": eval_loss})

    def epoch_done(self, **kwargs):
        train_losses = map(
            lambda x: x["train_loss"],
            filter(
                lambda x: x["epoch"] == self.epoch,
                self.train_step_log,
            ),
        )
        eval_losses = map(
            lambda x: x["eval_loss"],
            filter(
                lambda x: x["epoch"] == self.epoch,
                self.eval_step_log,
            ),
        )
        epoch_result = {
            "epoch": self.epoch,
            "train_loss": np.mean(train_losses),
            "eval_loss": np.mean(eval_losses),
            **kwargs,
        }
        print(", ".join([f"{k}: {v}" for k, v in epoch_result.items()]))
        self.epoch_log.append(epoch_result)
        return epoch_result
