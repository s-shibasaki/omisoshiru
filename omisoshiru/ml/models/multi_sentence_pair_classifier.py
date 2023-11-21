from typing import List

import torch
from torch import nn
from transformers import AutoModel, AutoTokenizer

from .multi_sentence_sum import MultiSentenceSum


class MultiSentencePairClassifier(nn.Module):
    def __init__(self, pretrained_model_name):
        """
        Initializes an instance of the MultiSentenceSum model.

        Args:
            pretrained_model_name (str): The name of a pre-trained transformer model.
        """
        super().__init__()
        self._multi_sentence_sum = MultiSentenceSum(pretrained_model_name)
        self._classifier = nn.Linear(self._multi_sentence_sum.hidden_size * 2, 1)
        self._dropout = nn.Dropout(0.1)
        self._sigmoid = nn.Sigmoid()

    def forward(
        self,
        sentences_a: List[List[str]],
        sentences_b: List[List[str]],
        weights_a: torch.Tensor,
        weights_b: torch.Tensor,
    ):
        sum_a = self._multi_sentence_sum(sentences_a, weights_a)
        sum_b = self._multi_sentence_sum(sentences_b, weights_b)
        concatenated = torch.cat((sum_a, sum_b), dim=1)
        logits = self._classifier(self._dropout(concatenated))
        output = self._sigmoid(logits).squeeze(1)
        return output
