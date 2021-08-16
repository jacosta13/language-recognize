import re
from typing import List
from unidecode import unidecode

from .constants import MAX_TEXT_LEN


def normalize_text(text: str) -> str:
    """
    Normalize text for model. This consists of removing non ASCII characters
    and some punctuation and special characters, and truncating to a maximum
    length.
    :param text: Input text.
    :return: Processed text.
    """
    clean = re.sub(r"[\s_()\-,:;%&]+", " ", unidecode(text))
    return clean[:MAX_TEXT_LEN]


def str_to_codes(text: str, pad_length: int = MAX_TEXT_LEN) -> List[int]:
    """
    Converts a given string to the list of integer Unicode codes of the
    characters.
    :param text: Normalized string.
    :param pad_length: Length to which to pad the list wih zeros. Padding is
        applied at the start pf the sequence.
    :return: List of integers.
    """
    codes = [ord(char) for char in text[:pad_length]]
    codes = [0 for _ in range(pad_length - len(codes))] + codes
    return codes
