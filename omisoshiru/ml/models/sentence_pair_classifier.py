from typing import List

import torch
import transformers
from torch import nn


class SentencePairClassifier(nn.Module):
    TOKENIZATION_OPTIONS = {
        "return_tensors": "pt",
        "padding": True,
        "truncation": True,
    }

    def __init__(self, pretrained_model_name):
        super().__init__()
        self._model = transformers.AutoModel.from_pretrained(pretrained_model_name)
        self._tokenizer = transformers.AutoTokenizer.from_pretrained(
            pretrained_model_name
        )
        self._classifier = nn.Linear(self._model.config.hidden_size, 1)
        self._dropout = nn.Dropout(0.1)

    def forward(self, sentence_a: List[str], sentence_b: List[str]):
        # Tokenize the input sentences
        inputs = self._tokenizer(
            sentence_a, sentence_b, **self.TOKENIZATION_OPTIONS
        ).to(next(self._model.parameters()).device)

        # Pass the tokenized input through the transformer model and extract pooled output
        model_output = self._model(**inputs).pooler_output
        logits = self._classifier(self._dropout(model_output))
        output = logits.squeeze(1)

        return output
