#!/bin/bash

import os


def remove_lines_with_only_dash(file_path):
    """Read the existing content of the file"""
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line for line in file if line.strip() != '---']

    # Write the modified content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)


if __name__ == "__main__":
    FOLDER_PATH = "/home/ofoo/Dev/md_project/arts_copy"  # Replace this with the path to your folder

    # Process each file in the folder
    for file_name in os.listdir(FOLDER_PATH):
        FILE_PATH = os.path.join(FOLDER_PATH, file_name)

        # Skip directories, process only files
        if not os.path.isfile(FILE_PATH):
            continue

        remove_lines_with_only_dash(FILE_PATH)
