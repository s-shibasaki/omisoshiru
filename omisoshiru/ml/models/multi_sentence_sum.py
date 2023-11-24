from typing import List

import torch
from torch import nn
from transformers import AutoModel, AutoTokenizer


class MultiSentenceSum(nn.Module):
    TOKENIZATION_OPTIONS = {
        "return_tensors": "pt",
        "padding": True,
        "truncation": True,
    }

    def __init__(self, pretrained_model_name):
        """
        Initializes an instance of the MultiSentenceSum model.

        Args:
            pretrained_model_name (str): The name of a pre-trained transformer model.
        """
        super().__init__()
        self._model = AutoModel.from_pretrained(pretrained_model_name)
        self._tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name)
        self.hidden_size = self._model.config.hidden_size

    def forward(self, sentences: List[List[str]], weights: torch.Tensor):
        """
        Forward pass of the MultiSentenceSum model.

        Args:
            sentences (List[List[str]]): A list of sentences where each sentence is represented
                as a list of strings. Shape: (num_batches, num_sentences).
            weights (torch.Tensor): A tensor containing weights for each sentence. The weights
                should have the same shape as the 'sentences' input. Shape: (num_batches, num_sentences).

        Returns:
            torch.Tensor: Weighted sum of the pooled outputs from the transformer model for each sentence.
                The output tensor has the shape (num_batches, hidden_size), where hidden_size
                depends on the transformer model architecture.
        """
        output_pool = []
        for sentence in zip(*sentences):
            # Tokenize the input sentences
            inputs = self._tokenizer(sentence, **self.TOKENIZATION_OPTIONS).to(
                next(self._model.parameters()).device
            )

            # Pass the tokenized input through the transformer model and extract pooled output
            output_pool.append(self._model(**inputs).pooler_output)

        # Stack the pooled outputs and apply weights
        weighted_outputs = torch.stack(output_pool) * weights.permute(1, 0).unsqueeze(
            -1
        )

        return weighted_outputs.sum(dim=0)
