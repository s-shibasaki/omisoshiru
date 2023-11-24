import pytest
import torch

from omisoshiru.ml.models import SentencePairClassifier

# ダミーデータの作成
dummy_sentence_a = ["This is sentence A."]
dummy_sentence_b = ["This is sentence B."]


@pytest.fixture
def sentence_pair_classifier():
    return SentencePairClassifier(pretrained_model_name="bert-base-uncased")


def test_forward_returns_tensor(sentence_pair_classifier):
    output = sentence_pair_classifier(dummy_sentence_a, dummy_sentence_b)
    assert isinstance(output, torch.Tensor)


def test_forward_shape(sentence_pair_classifier):
    output = sentence_pair_classifier(dummy_sentence_a, dummy_sentence_b)
    assert output.shape == torch.Size([1])
