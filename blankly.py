#!/bin/python
""" remove white spaces and linebreaks and blank lines
"""
import os
import re

# Set the path to the folder containing the files to serve
FOLDER_PATH = "/home/ofoo/Dev/md_project/md/"

FILES = {}
line_reg_ex = r"^\s*$"


def strip_blank_lines(file_path):
    """Read the existing content of the file"""
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Filter out lines with only "---"
    lines = [line for line in lines if not re.match(r"^\s*$", line)]

    # Write the modified content back to the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(lines)


if __name__ == "__main__":
    FOLDER_PATH = "/home/ofoo/Dev/md_project/md/"
    for file_name in os.listdir(FOLDER_PATH):
        if file_name.endswith(".md"):
            FILES[file_name] = FOLDER_PATH + file_name
            strip_blank_lines(FILES[file_name])
