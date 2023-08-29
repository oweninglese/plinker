#!/usr/bin/python
"""tools.py - tools for tags and links.

Returns:
_type_: None
"""
import csv
from datetime import date
import os
import re
from typing import Any, Match, Pattern
import markdown
import frontmatter as fm


def read_tags_from_csv(file_path):
    """
    Reads tags from a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        list: A list of tags read from the CSV file.
    """
    tagslist = []
    with open(file_path, "r", encoding="utf-8") as t_f:
        data = t_f.read()
        tagslist = data.split(",")
        tagslist = [x.strip() for x in tagslist]

    return tagslist


TAGS = read_tags_from_csv("tagfile.csv")
ARTS = "/home/ofoo/Dev/md_project/md/"

CLEARTAGS = [tag.strip(" ") for tag in TAGS]
while "" in CLEARTAGS:
    CLEARTAGS.remove("")


def checkforend(testfile: str) -> Match[str]:
    """
    Check the end of the yaml file for the end of the training session.

    @param tfi - the yaml file to check for the end of the training session.
    @returns the end of the yaml file.
    """

    def endof_yaml(file: list[str]) -> Any:
        """
        Given a file, return the end of the yaml frontmatter.

        Args:
                file (str): full file contents
        Returns:
            func: return position of end of yaml frontmatter
        """
        abc: Pattern = re.compile("---")
        return search_yaml(file, abc)

    def search_yaml(file: list[str], anyre: Pattern) -> list[int]:
        """
        Search the markdown file for the end of the frontmatter.

        Return the index of the end of the file.
        @param file - the yaml file to search for the end of the file.
        @param a - the pattern to search for in the file.
        @return the index of the end of the file.
        """
        end: list = []
        for i, nii in enumerate(file, 1):
            if anyre.search(nii):
                end = i
        return end

    with open(testfile, "r", encoding="utf-8") as file:
        text = file.readlines()
        end: Match[str] = endof_yaml(text)
    return end


def link_tags(file, tag):
    """
    Generate the function comment for the given function body.

    This function generates a function comment for the given function body
    using the provided template.
    It takes the function body as input and returns the generated function
    comment as output.

    @param file: The file to process.
    @param tag: The tag to check for and replace.

    @return: None
    """
    CHECKED = set()

    def add_tag(afile: str, tag: str) -> bool:
        """
        Check if the tag is in the post.

        If it is, add the tag to the post's tags.
        Also, write the post to the file.

        @param afile - the file to write to
        @param tag - the tag to check for
        """
        if not os.path.isfile(ARTS + afile):
            print(f"File '{afile}' not found.")
            return False

        # print(f"checking for tag '{tag}' in '{afile}'.")
        post = fm.load(ARTS + afile)
        yaml = post.metadata.get('tags', [])
        if yaml is None:
            post["tags"] = ''
        if tag in post.content:
            post["tags"] += " " + str(tag)
            print(f"Found and Adding tag '{tag}' to '{afile}'.")
            with open(ARTS + afile, "w", encoding="utf-8") as text:
                text.write(fm.dumps(post))
            return True
        else:
            return False

    def resub(tag: str, line: str) -> str:
        """Return line with string substitution made adding brackets.

        Args:
            tag (str): tag to be replaced
            line (str): line to be searched

        Returns:
            str: line with tag replaced
        """
        tag = re.escape(tag)
        return re.sub(tag, f"[[{tag}]]", line)

    def enum_and_sub(testfile, abc, tag):
        """
        Enumerate the source file and replace the lines with the new tag.

        @param testfile - the file to enumerate and replace lines in.
        @param abc - the number of lines to skip.
        @param subs - the number of lines to replace.
        @param tag - the tag to replace with.
        """
        with open(ARTS + testfile, "r", encoding="utf-8") as file:
            text = file.readlines()
        with open(ARTS + testfile, "w", encoding="utf-8") as source:
            for i, k in enumerate(text):
                if i < abc:
                    source.write(k)
                else:
                    line = resub(tag, k)
                    if line is not None:
                        source.write(line)

    if add_tag(file, tag) and tag not in CHECKED:
        print(f'Added tag "{tag}" to "{file}".')
        print(f"Attempting to update tags in {file} content")
        enum_and_sub(file, checkforend(ARTS + file), tag)
        CHECKED.add(tag)


def check_files(file, tag):
    """
    Check the files in the arts folder.
    """
    if file.endswith(".md"):
        link_tags(file, tag)


if __name__ == "__main__":
    for ff in os.listdir(ARTS):
        if ff.endswith(".md"):
            check_files(ff, CLEARTAGS)
