#!/bin/bash
"""SpellChecker correction
"""

import os
from google_spell_checker import GoogleSpellChecker  # Correct the import statement


def spell_check_and_auto_correct_string(input_string):
    """Create a SpellChecker instance"""
    spell = GoogleSpellChecker()

    # Split the input string into words
    words = input_string.split()

    # Find misspelled words
    misspelled = [spell.check(i) for i in words if not spell.check(i)]

    # Filter out None values
    correct = [c for c in misspelled if c is not None]

    # Combine the corrected words back into a string
    corrected_string = " ".join(correct)
    return corrected_string

def spell_check_and_auto_correct_file(file_path: str) -> str:
    """
    Reads the content of the file located at `file_path` and performs
    spellcheck and auto-correct on it.

    Args:
        file_path (str): The path of the file to be read.

    Returns:
        str: The corrected content of the file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    corrected_content = spell_check_and_auto_correct_string(content)
    return corrected_content

if __name__ == "__main__":
    FOLDER_PATH = "/home/ofoo/Dev/md_project/arts_copy/"
    for FILE_PATH in os.listdir(FOLDER_PATH):
        if FILE_PATH.endswith(".md"):
            print(f"correcting file: {FILE_PATH}")
            FILE = os.path.join(FOLDER_PATH, FILE_PATH)  # Use os.path.join for file paths
            CORRECTION = spell_check_and_auto_correct_file(FILE)
            # Write the corrected content back to the file
            with open(FILE, "w", encoding="utf-8") as file:
                file.write(CORRECTION)
            print(f"Auto-corrected file content: {FILE}")
