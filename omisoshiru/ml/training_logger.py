from dataclasses import dataclass, field
from typing import Dict, List, Union

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from dataclass_wizard import YAMLWizard


@dataclass
class TrainingLogger(YAMLWizard):
    epoch: int = field(default=-1)
    train_step_log: List[Dict[str, float]] = field(default_factory=list)
    eval_step_log: List[Dict[str, float]] = field(default_factory=list)
    epoch_log: List[Dict[str, float]] = field(default_factory=list)

    def epoch_init(self):
        self.epoch += 1

    def train_step(self, train_loss):
        self.train_step_log.append({"epoch": self.epoch, "train_loss": train_loss})

    def eval_step(self, eval_loss):
        self.eval_step_log.append({"epoch": self.epoch, "eval_loss": eval_loss})

    def epoch_done(self, **kwargs):
        train_losses = list(
            map(
                lambda x: x["train_loss"],
                filter(
                    lambda x: x["epoch"] == self.epoch,
                    self.train_step_log,
                ),
            ),
        )
        eval_losses = list(
            map(
                lambda x: x["eval_loss"],
                filter(
                    lambda x: x["epoch"] == self.epoch,
                    self.eval_step_log,
                ),
            )
        )
        epoch_result = {
            "epoch": self.epoch,
            "train_loss": float(np.mean(train_losses)),
            "eval_loss": float(np.mean(eval_losses)),
            **kwargs,
        }
        print(", ".join([f"{k}: {v}" for k, v in epoch_result.items()]))
        self.epoch_log.append(epoch_result)
        return epoch_result

    def epoch_plot(self, variables=None, log=False):
        sns.set(style="whitegrid", palette="deep", context="paper")
        if variables is None:
            variables = ["train_loss", "eval_loss"]
        df = pd.DataFrame(self.epoch_log).melt("epoch", variables)
        sns.lineplot(x="epoch", y="value", hue="variable", data=df)
        if log:
            plt.yscale("log")
        plt.show()
