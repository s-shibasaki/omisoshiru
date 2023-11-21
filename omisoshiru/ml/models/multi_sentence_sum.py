from typing import List

import torch
from torch import nn
from transformers import AutoModel, AutoTokenizer


class MultiSentenceSum(nn.Module):
    def __init__(self, pretrained_model_name):
        super().__init__()
        self._model = AutoModel.from_pretrained(pretrained_model_name)
        self._tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name)
        self._tokenization_options = {
            "return_tensors": "pt",
            "padding": True,
            "truncation": True,
        }

    def forward(self, sentences: List[List[str]], weights: torch.Tensor):
        """_summary_

        Args:
            sentences (List[List[str]]): shape: (num_sentences, num_batches)
            weights (torch.Tensor): shape: (num_sentences, num_batches)

        Returns:
            _type_: _description_
        """
        output_pool = []
        for sentence in sentences:
            inputs = self._tokenizer(sentence, **self._tokenization_options)
            output_pool.append(self._model(**inputs).pooler_output)
        print(output_pool[0].size())
        weighted_outputs = torch.stack(output_pool) * weights.unsqueeze(-1)
        return weighted_outputs
