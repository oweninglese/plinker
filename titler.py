#!/bin/python
"""insert filename in title: yaml
"""
import os


def insert_filename_in_title_lines(file_path):
    """
    Inserts the filename without extension into the 'title'
    metadata line of each file in the given folder.

    Args:
        folder_path (str): The path to the folder containing the files.
    """

    def replace_underscores_with_spaces(input_string):
        """
        Replaces underscores with spaces in the given input string.

        Args:
        input_string (str): The input string to process.

        Returns:
        str: The input string with underscores replaced by spaces.
        """
        # Use the `replace` method to replace all underscores with spaces
        return input_string.replace("_", " ")

        # Skip if the path is not a file

        # Read the lines of the file
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

        # Write the modified lines back to the file
    with open(file_path, "w", encoding="utf-8") as file:
        for line in lines:
            # Check if the line starts with "title:"
            if line.strip().startswith("title:"):
                    # Get the filename without extension
                filename_without_extension = os.path.splitext(file_path)[0]
                filename_without_path =  os.path.basename(filename_without_extension)

                    # Replace the line with the modified line
                line = f"title: {filename_without_path}\n"
                line = replace_underscores_with_spaces(line)
                # Write the line to the file
                file.write(line)
                continue
            file.write(line)


if __name__ == "__main__":
    FOLDER_PATH = (
        "/home/ofoo/Dev/md_project/md/"  # Replace this with your folder path
    )
    insert_filename_in_title_lines(FOLDER_PATH)
