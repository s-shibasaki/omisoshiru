from typing import Optional

import MeCab
import unidic_lite


class Wakachi:
    def __init__(self, allow_whitespace: Optional[bool] = None):
        """
        A class for tokenizing Japanese text using MeCab.

        Args:
            allow_whitespace (Optional[bool]): If True, whitespace characters are allowed in the input text.
                If False, an error will be raised if whitespace characters are present.
                Defaults to None, in which case the default behavior is False.

        Examples:
            >>> wakachi = Wakachi(allow_whitespace=True)
            >>> input_text = "これはテストです。"
            >>> tokens = wakachi.parse(input_text)
            >>> print(tokens)
            ['これ', 'は', 'テスト', 'です', '。']
        """
        dicdir = unidic_lite.DICDIR.replace("\\", "/")
        self.__wakachi = MeCab.Tagger(f"-Owakati -d {dicdir}")
        self.allow_whitespace = (
            allow_whitespace if allow_whitespace is not None else False
        )

    def parse(self, string: str):
        """
        Tokenizes the input string using MeCab.

        Args:
            string (str): The input text to be tokenized.

        Returns:
            list: A list of tokens obtained by tokenizing the input text.

        Raises:
            ValueError: If 'allow_whitespace' is False, and the input string contains whitespace characters.
        """
        if not self.allow_whitespace and any(c.isspace() for c in string):
            raise ValueError(
                "If 'allow_whitespace' is False, the input string must not contain whitespace characters."
            )
        return self.__wakachi.parse(string).split()
