from typing import List, Union

import mojimoji


def unify_hz(text: Union[str, List[str]]):
    if isinstance(text, List):
        return [unify_hz(item) for item in text]

    else:
        text = mojimoji.han_to_zen(text, ascii=False, digit=False, kana=True)
        text = mojimoji.zen_to_han(text, ascii=True, digit=True, kana=False)
        return text
