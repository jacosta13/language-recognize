from typing import Dict, Any

from . import constants, utils
from ..exceptions import InputValidationErr


class LangRecModelHandler:
    """
    Handler for the language recognition model.

    Methods
    -------
    - identify_lang
    """

    def __init__(self, pad_length: int = constants.MAX_TEXT_LEN, min_len: int = 8):
        self.pad_length = pad_length
        self.min_len = min_len

    def validate_input(self, text: str):
        """
        Validates the input text.
        :param text: Input text.
        :return: None.
        """
        # Chack min length
        if len(text) < self.min_len:
            raise InputValidationErr(
                "Input text is too short! Minimum length is %d" % self.min_len
            )

    def identify_lang(self, text: str) -> Dict[str, Any]:
        """
        Run the given text by the model and return the result.
        :param text: Input text.
        :return: Dictionary.
            Keys
            ----
            - language: (String) name of the language the text is written in
              according to the model.
            - confidence: (Float) how confident the model is in the
              classification (softmax output).
        """
        self.validate_input(text)
        processed_text = utils.normalize_text(text)
        codes = utils.str_to_codes(processed_text)
        print("INPUT LENGTH: %d" % len(codes))

        # TODO: Implement model call

        out = {
            "language": "Gibberish",
            "confidence": 0.99
        }
        return out

