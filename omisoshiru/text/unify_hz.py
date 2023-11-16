from typing import List, Literal, Optional, Union

import mojimoji


def unify_hz(
    text: Union[str, List[str]],
    on_error: Optional[Literal["raise", "return_empty", "return_none"]] = "raise",
):
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
