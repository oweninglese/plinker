
def read_file_into_string(filepath):
    """
    Read the contents of a file into a string.

    Parameters:
        file_path (str): The path to the file to be read.

    Returns:
        str: The contents of the file as a string.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        contents = file.read()
    return contents


def break_string_into_lines(input_string, words_per_line):
    """
    Takes an input string and breaks it into lines, with a specified number
    of words per line.

    Parameters:
        input_string (str): The string to be broken into lines.
        words_per_line (int): The number of words per line.

    Returns:
        list: A list of strings, where each string represents
        a line containing the specified number of words.
    """
    words = input_string.split()
    lines = [' '.join(words[i:i + words_per_line]) for i in range(0, len(words), words_per_line)]
    return lines


def write_lines_to_file(filepath, lines):
    """
    Write multiple lines to a file.

    Args:
        file_path (str): The path to the file to write the lines to.
        lines (List[str]): A list of strings representing the lines to write.

    Returns:
        None
    """
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write('\n'.join(lines))


def process_file_and_write_lines(filepath, words_per_line):
    """
    Process a file and write its contents to a new file,
    with a specified number of words per line.

    :param file_path: The path to the input file.
    :type file_path: str
    :param words_per_line: The number of words to be
    written per line in the output file.
    :type words_per_line: int
    """
    contents = read_file_into_string(filepath)
    lines = break_string_into_lines(contents, words_per_line)
    write_lines_to_file(file_path, lines)


if __name__ == "__main__":
    ARTS = '/home/ofoo/Dev/md_project/arts_copy'
    CHUNK = 12
    for file_path in ARTS:
        process_file_and_write_lines(file_path, CHUNK)
