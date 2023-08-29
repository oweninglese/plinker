#! /usr/bin/python
import os

import frontmatter as fm


ARTS = "/home/ofoo/Dev/md_project/md/"


def open_file(file):
    """
    Open a file and load its content.

    Args:
        file (str): The path to the file to be opened.

    Returns:
        The content of the file.

    """
    print(f"Attempting to open file: {file}")
    post = fm.load(ARTS + file)
    return post


def write_yaml(file, section):
    """
    Writes the provided 'section' to the YAML front matter of
    the specified 'file'.

    Parameters:
        file (str): The path to the file to write the YAML front matter to.
        section (dict): The section to write to the YAML front matter.

    Returns:
        None
    """
    post = open_file(file)
    with open(ARTS + file, "w", encoding="utf-8") as text:
        post.metadata = section
        text.write(fm.dumps(post))


def write_content(file, section):
    """
    Write the content of a section to a file.

    Parameters:
        file (str): The name of the file to write the content to.
        section (str): The content to be written to the file.

    Returns:
        None
    """
    post = open_file(file)
    with open(ARTS + file, "w", encoding="utf-8") as text:
        post.content = section
        text.write(fm.dumps(post))


def content(file):
    """
    Get the content of a file.

    :param file: The path of the file.
    :type file: str
    :return: The content of the file.
    :rtype: str
    """
    post = open_file(file)
    return post.content


def metadata(file):
    """
    Get the metadata of a file.

    Args:
        file (str): The path to the file.

    Returns:
        dict: The metadata of the file.
    """
    post = open_file(file)
    return post.metadata


def clean_metadata(file):
    post = open_file(file)
    second_dash_index = content.find('---', content.find('---') + 3)

    if second_dash_index != -1:
        cleaned_content = content[second_dash_index + 3:]
        return post.write(cleaned_content)


def prep_file(file):
    """
    This function prepares a file by writing YAML contents to it.

    Args:
        file (str): The path of the file to be prepared.

    Returns:
        None
    """
    post = fm.load(ARTS + file)
    post['title'] = ''
    post['created'] = ''
    post['author'] = ''
    post['source'] = ''
    post['tags'] = ''
    write_yaml(file, post.metadata)


if __name__ == "__main__":
    for md in os.listdir(ARTS):
        if md.endswith(".md"):
            clean_metadata(md)
            prep_file(md)
