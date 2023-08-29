#!/bin/python

"""Join lines with less than 80 max length chars
"""


def join_lines_with_max_length(lines, max_length=122):
    """
    Joins a list of lines into a list of lines
    where each line has a maximum length of 'max_length'.

    Args:
        lines (list): The list of lines to be joined.
        max_length (int, optional): The maximum length
        allowed for each line. Defaults to 100.

    Returns:
        list: The list of lines with maximum length.
    """
    result_lines = []
    current_line = ""

    for line in lines:
        if len(current_line) + len(line) <= max_length:
            current_line += line
        else:
            result_lines.append(current_line)
            current_line = line

    if current_line:
        result_lines.append(current_line)

    return result_lines
