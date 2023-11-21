from typing import List

import torch
from torch import nn
from transformers import AutoModel, AutoTokenizer


class MultiSentenceSum(nn.Module):
    def __init__(self, pretrained_model_name):
        super().__init__()
        self._model = AutoModel.from_pretrained(pretrained_model_name)
        self._tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name)

    def forward(self, sentences_batch: List[List[str]]):
        last_hidden_states = []
        for sentence_batch in sentences_batch:
            inputs = self._tokenizer(sentence_batch)
            outputs = self._model(**inputs)
            last_hidden_states.append(outputs.last_hidden_states)
        return torch.stack(last_hidden_states).sum(dim=0)
