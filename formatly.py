#!/bin/python
"""Format string lines joined at 80 chars
"""

import os
import textwrap
import combiner


def formatter(file_path):
    """Open a file, wrap lines at 100 characters
    and write changes back to the file.

    Args:
        file_path (str): Path to the file to be formatted.
    """
    # Open the file in read mode
    with open(file_path, "r") as file:
        # Read all lines from the file
        lines = file.readlines()
        # Format each line by wrapping it at 100 characters
        formatted_lines = [textwrap.fill(line.strip(), 100) for line in lines]
        formatted_lines = combiner.join_lines_with_max_length(formatted_lines)

    # Open the file in write mode
    with open(file_path, "w") as file:
        # Write the formatted lines back to the file
        file.writelines(formatted_lines)


if __name__ == "main":
    FOLDER_DIR = "home/ofoo/Dev/md_project/arts_copy/"
    md = "".endswith(".md")
    for md in os.listdir(FOLDER_DIR):
        formatter(md)
