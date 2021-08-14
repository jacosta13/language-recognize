from typing import List, Dict
from unidecode import unidecode


class CharTokenizer:
    """
    Tokenizer for character-level embeddings and analysis.
    """

    LETTERS: List[str] = [
        'A',
        'a',
        'B',
        'b',
        'C',
        'c',
        'D',
        'd',
        'E',
        'e',
        'F',
        'f',
        'G',
        'g',
        'H',
        'h',
        'I',
        'i',
        'J',
        'j',
        'K',
        'k',
        'L',
        'l',
        'M',
        'm',
        'N',
        'n',
        'O',
        'o',
        'P',
        'p',
        'Q',
        'q',
        'R',
        'r',
        'S',
        's',
        'T',
        't',
        'U',
        'u',
        'V',
        'v',
        'W',
        'w',
        'X',
        'x',
        'Y',
        'y',
        'Z',
        'z'
    ]

    DIGITS: List[str] = [str(i) for i in range(10)]

    def __init__(self):
        self.__inverse_mapping = dict(
            enumerate(self.LETTERS + self.DIGITS + ["[UNK]"], start=1)
        )
        self.__mapping = {v: k for k, v in self.__inverse_mapping}
        self.__unk_token = self.__mapping["[UNK]"]

    @property
    def mapping(self) -> Dict[str, int]:
        """
        Char -> index mapping (Read-only).
        """
        return self.__mapping

    @property
    def inverse_mapping(self) -> Dict[int, str]:
        """
        Index -> Char mapping (Read-only).
        """
        return self.__inverse_mapping

    @property
    def unk_token(self) -> int:
        """
        Token to assign to unknown characters.
        """
        return self.__unk_token

    def string_to_tokens(self, string: str, decode: bool = False) -> List[int]:
        """
        Convert a string to a list of integer tokens.
        :param string: Input string.
        :param decode: Apply unidecode to remove non ascii characters before
            tokenizing or not. Must be done to avoid unknown characters.
        :return: List of integers.
        """
        if decode:
            string = unidecode(string)

        return [self.mapping.get(c, self.unk_token) for c in list(string)]
