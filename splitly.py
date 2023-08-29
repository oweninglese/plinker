#!/bin/python

"""Spltlines at 80 chars
"""

import os


FILES = {}


def split_lines_at_n_chars(file_path):
    """
    Split the lines in a file at every 100 characters.

    Args:
        file_path (str): The path to the file.

    Returns:
        None
    """
    # Read the content of the file
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    lines = []
    # Split each line at every 100 characters and add them to the lines list
    for line in content.splitlines():
        for i in range(0, len(line), 100):
            lines.append(line[i : i + 100])

    # Overwrite the file with the new lines
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))


if __name__ == "__main__":
    FOLDER_PATH = "/home/ofoo/Dev/arts_copy/"
    for file_name in os.listdir(FOLDER_PATH):
        if file_name.endswith(".md"):
            FILES[file_name] = FOLDER_PATH + file_name
            split_lines_at_n_chars(FILES[file_name])
