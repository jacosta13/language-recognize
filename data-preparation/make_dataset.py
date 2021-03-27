import os
import re
import pandas as pd
from unidecode import unidecode

#: Mapping csv name -> language name. Take languages with LATIN ALPHABET.
LANG_FILES = {
    "ted_talks_en.csv": "English",
    "ted_talks_fr.csv": "French",
    "ted_talks_it.csv": "Italian",
    "ted_talks_pt-br.csv": "Portuguese",
    "ted_talks_tr.csv": "Turkish"
}


def process_text(text: str, output_filename: str):
    """
    Takes a single text, processes it and saves it by lines in a text file.
    :param text: Text to process (one talk).
    :param output_filename: File (.txt) to store the output.
    :return:
    """
    pass


def process_file(
        file_path: str,
        language_name: str,
        col_name: str = "transcript",
        output_path: str = os.path.join("data", "processed-text")):
    """
    Process a csv from the TED talks dataset corrsponding to the dataset for
    one language. Saves the result as text files within a folder with the
    language name. Diacritics are removed using unidecode before saving.
    :param file_path: Path of the file to process.
    :param language_name: Name of the language for output.
    :param col_name: Name of the column that contains the text to process.
    :param output_path: Directory where output will be stored.
    :return: None
    """
    pass


def prepare_dataset(
        input_dir: str,
        output_dir: str = os.path.join("data", "processed-text"),
        col_name: str = "transcript"):
    """
    Prepares the dataset for the model. Output is stored as follows:

    output_dir
      - Language1
        - Text1.txt
        - Text2.txt
        ...
      - Language2
        - Text1.txt
        ...

    This is done to make it compatible with TensorFlow Text Line Dataset.
    :param input_dir: Directory where raw input csv files are stored. Their
        names must correspond to the keys of LANG_FILES.
    :param output_dir: Directory where outputs will be stored.
    :param col_name: Name of column containing the text in the csv.
    :return: None
    """
    if not os.path.isdir(input_dir):
        raise FileNotFoundError(
            f"Could not find input directory '{input_dir}'"
        )
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    for k, v in LANG_FILES.items():
        full_path = os.path.join(input_dir, k)

        # Check that the file exists
        if os.path.isfile(full_path):
            process_file(
                full_path,
                language_name=v,
                col_name=col_name,
                output_path=output_dir
            )
        else:
            print(f"ERROR: File '{full_path}' not found.")
            continue


if __name__ == '__main__':
    # Use Fire to run from terminal
    import fire
    fire.Fire(prepare_dataset)
