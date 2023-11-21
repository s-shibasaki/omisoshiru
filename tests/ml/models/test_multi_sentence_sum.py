import pytest
import torch

from omisoshiru.ml.models import MultiSentenceSum


@pytest.fixture
def model():
    return MultiSentenceSum("bert-base-uncased")


@pytest.mark.slow
def test_forward_pass_single_sentence(model):
    sentences = [["This is a test.", "Another sentence."]]
    weights = torch.tensor([[0.5, 0.7]])

    result = model.forward(sentences, weights)

    # Add assertions based on the expected behavior of your forward method
    assert result.shape == torch.Size(
        [1, 768]
    )  # Replace 768 with the actual hidden_size of your model


@pytest.mark.slow
def test_forward_pass_multiple_sentences(model):
    sentences = [
        ["This is a test.", "Another sentence."],
        ["Yet another example.", "Testing multiple sentences."],
    ]
    weights = torch.tensor([[0.5, 0.7], [0.3, 0.6]])

    result = model.forward(sentences, weights)

    # Add assertions based on the expected behavior of your forward method
    assert result.shape == torch.Size(
        [2, 768]
    )  # Replace 768 with the actual hidden_size of your model


@pytest.mark.slow
def test_hidden_size(model):
    assert model.hidden_size == 768


if __name__ == "__main__":
    pytest.main()
