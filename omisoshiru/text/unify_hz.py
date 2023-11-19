from typing import List, Literal, Optional, Union

import mojimoji


def unify_hz(
    text: Union[str, List[str]],
    on_error: Optional[Literal["raise", "return_empty", "return_none"]] = "raise",
) -> Union[str, List[str]]:
    """
    Unify the character width in the input text to either full-width or half-width.

    Args:
        text (Union[str, List[str]]): The input text or list of texts to be processed.
        on_error (Optional[Literal]): Specifies the
            behavior in case of invalid input type. Defaults to "raise".<br />
            "raise": Raises a TypeError for invalid input type.<br />
            "return_empty": Returns an empty string or list.<br />
            "return_none": Returns None.<br />

    Returns:
        Union[str, List[str]]: The text or list of texts with unified character width.

    Examples:
        >>> # Example with a single string
        >>> original_text = "Ｈｅｌｌｏ, １２３."
        >>> modified_text = unify_hz(original_text)
        >>> print(modified_text)
        "Hello, 123."

        >>> # Example with a list of strings
        >>> original_texts = ["Ｈｅｌｌｏ", "１２３."]
        >>> modified_texts = unify_hz(original_texts)
        >>> print(modified_texts)
        ["Hello", "123."]
    """
    if isinstance(text, List):
        return [unify_hz(item) for item in text]

    elif isinstance(text, str):
        text = mojimoji.han_to_zen(text, ascii=False, digit=False, kana=True)
        text = mojimoji.zen_to_han(text, ascii=True, digit=True, kana=False)
        return text

    elif on_error == "raise":
        raise TypeError(
            "Invalid input type: 'text' must be a string or a list of strings"
        )
    elif on_error == "return_empty":
        return ""
    elif on_error == "return_none":
        return None
    else:
        raise ValueError("Invalid error handling type")
