#1 /usr/bin/python



import os

#! /usr/bin/python

#

import glob
import os
import re
import datetime
import frontmatter as fm


def update_yml(file):
    """
    Update the YAML file with the provided content.

    Parameters:
        file (str): The path to the YAML file.
        content (str): The content to be updated.

    Returns:
        None
    """

    with open(file, "r", encoding="utf-8") as fr:
        full_file = fr.read()
        post = fm.load(file)
        created = datetime.datetime.now().strftime("%Y-%m-%d")
        post.metadata['created'] = created.lstrip()

    with open(file, "w", encoding="utf-8") as fw:
        fw.write(fm.dumps(post))
    # print(f"Updated file: {file} with stable URL: {datetime.date.today()}")


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


FILES = get_files_in_folder("/home/ofoo/Dev/md_project/md/")

for ff in FILES:
    update_yml(ff)
