import pytest
import torch

from omisoshiru.ml.models import MultiSentencePairClassifier


@pytest.fixture
def model():
    return MultiSentencePairClassifier("bert-base-uncased")


@pytest.mark.slow
def test_forward_pass_single_sentence(model):
    sentences_a = [["This is a test.", "Another sentence."]]
    weights_a = torch.tensor([[0.5, 0.7]])

    sentences_b = [["Yet another example.", "Testing multiple sentences."]]
    weights_b = torch.tensor([[0.3, 0.6]])

    result = model.forward(sentences_a, sentences_b, weights_a, weights_b)

    # Add assertions based on the expected behavior of your forward method
    assert result.shape == torch.Size(
        [1]
    )  # Assuming binary classification, adjust accordingly


@pytest.mark.slow
def test_forward_pass_multiple_sentences(model):
    sentences_a = [
        ["This is a test.", "Another sentence."],
        ["Yet another example.", "Testing multiple sentences."],
    ]
    weights_a = torch.tensor([[0.5, 0.7], [0.3, 0.6]])

    sentences_b = [
        ["Another test.", "Additional sentence."],
        ["Yet another example.", "More sentences to test."],
    ]
    weights_b = torch.tensor([[0.4, 0.8], [0.2, 0.5]])

    result = model.forward(sentences_a, sentences_b, weights_a, weights_b)

    # Add assertions based on the expected behavior of your forward method
    assert result.shape == torch.Size(
        [2]
    )  # Assuming binary classification, adjust accordingly


if __name__ == "__main__":
    pytest.main()
