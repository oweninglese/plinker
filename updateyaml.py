#! /usr/bin/python

import os
import csv
import glob
import titler as ftitle
import creator as created
import source as sourcer
import authorer as author
import tagger as tagg


def get_files_in_folder(folder_path):
    """
    Get a list of files in a specified folder.

    Args:
        folder_path (str): The path to the folder.

    Returns:
        list: A list of file paths in the specified folder.
    """
    files = []
    for file_path in glob.glob(os.path.join(folder_path, "*")):
        if os.path.isfile(file_path):
            files.append(file_path)
    return files


def read_tags_from_csv():
    """
    Reads tags from a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        list: A list of tags read from the CSV file.
    """
    tagslist = []
    tags = 'tagfile.csv'
    with open(tags, "r", encoding="utf-8") as t_f:
        data = t_f.read()
        tagslist = data.split(",")
        tagslist = [x.strip() for x in tagslist]

    return tagslist


def main(file):
    """
     Update the metadata in the given file.

    :param file: The file to update the metadata in.
    :type file: str

    :return: None
    :rtype: None
    """
    print(f"Updating titles for {file}")
    ftitle.insert_filename_in_title_lines(file)

    print(f"Updating date for {file}")
    created.update_yml(file)

    print(f"Updating authors for {file}")
    author.update_yml(file)

    print(f"Updating sources for {file}")
    sourcer.update_yml(file)

    # print(f"Updating tags for {file}")
    # tagg.check_files(file, TAGS)


# TAGS = read_tags_from_csv("tagfile.csv")

FILES = get_files_in_folder("/home/ofoo/Dev/md_project/md")

for ff in FILES:
    main(ff)
