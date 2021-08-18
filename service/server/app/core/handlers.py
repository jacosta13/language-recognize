import os
import numpy as np
from typing import Dict, Any, List
import tflite_runtime.interpreter as tflite

from . import constants, utils
from ..exceptions import InputValidationErr


class LangRecModelHandler:
    """
    Handler for the language recognition model.

    Methods
    -------
    - identify_lang
    """

    LANGUAGES: List[str] = sorted([
        "English",
        "French",
        "Italian",
        "Portuguese",
        "Spanish",
        "Turkish"
    ])

    LITE_MODEL = tflite.Interpreter(os.path.join("assets", "model.tflite"))

    def __init__(
            self,
            pad_length: int = constants.MAX_TEXT_LEN,
            min_len: int = 8):
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

    def model_call(self, input_seq: List[int]) -> np.ndarray:
        """
        Use the model to perform inference on the given sequence.
        :param input_seq: Sequence of tokens (integers).
        :return: Numpy array of probabilities.
        """
        self.LITE_MODEL.allocate_tensors()
        input_detail = self.LITE_MODEL.get_input_details()
        output_detail = self.LITE_MODEL.get_output_details()

        self.LITE_MODEL.set_tensor(
            input_detail[0]["index"],
            np.array([input_seq], dtype="int32")
        )
        self.LITE_MODEL.invoke()
        output = self.LITE_MODEL.get_tensor(output_detail[0]["index"])
        return output

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
        # Preprocessing
        self.validate_input(text)
        processed_text = utils.normalize_text(text)
        codes = utils.str_to_codes(processed_text)

        # Model call
        model_out = self.model_call(codes)

        # Postprocessing
        out_flat = model_out.flatten()
        lang_conf = float(np.max(out_flat))
        lang_idx = np.argmax(out_flat)

        out = {
            "language": self.LANGUAGES[lang_idx],
            "confidence": lang_conf
        }
        return out

