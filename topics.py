import glob
import os

import frontmatter as fm


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
            print(file_path)
            files.append(file_path)
    return files


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
ARTS = "/home/ofoo/Dev/md_project/arts/md/"
TOPICS = "/home/ofoo/Dev/md_project/topics"
CLEARTAGS = [tag.strip(" ") for tag in TAGS]
while "" in CLEARTAGS:
    CLEARTAGS.remove("")
FILES = get_files_in_folder(ARTS)



def namefile(tag, encoding='utf-8'):
    """
    Creates empty files for each given tag in the specified directory.

    Args:
        file (str): The name of the file to check for each tag.
        tags (list): A list of tags to create empty files for.

    Returns:
        None
    """
    tag = str(tag)
    with open(os.path.join(TOPICS, f'{tag}.md'), 'a+', encoding=encoding) as f:
        f.write(f'#{tag}\n')
    return


def set_metadata(tags, encoding='utf-8'):
    """
    Sets metadata for each tag in the given list.

    Args:
        tags (list): A list of tags.
        encoding (str, optional): The encoding to be used. Defaults to 'utf-8'.

    Returns:
        None
    """
    for tag in tags:
        post = fm.load(os.path.join(TOPICS, f'{tags}.md'))
        post.metadata = {'tags': f'{tag}'}
        post.metadata = {'title': tag}
        post.metadata = {'author' : 'ofoo'}
        post.metadata = {'source' : 'ofoo'}
        post.metadata = {'created' : '2023-08-27'}
        fm.dumps(post)


def nametags(tag):
    namefile(tag)
    return


def metatags(tags):
    for tag in tags:
        set_metadata(tag)
    return


def run(file, tags):


    """
    Creates empty files for each given tag in the specified directory.

    Args:
        file (str): The name of the file to check for each tag.
        tags (list): A list of tags to create empty files for.

    Returns:
        None

    """
    for tag in tags:
        with open(os.path.join(TOPICS, f'{tag}.md'), 'a+', encoding='utf-8') as f:
            # print(f'Checking file: {file} for tag: {tag}')
            post = fm.load(os.path.join(ARTS, file))
            if tag in post.content:
                topics = ''
                topics += f"[[research/articles/{file[41:-3]}]]\n"
                f.write(topics)
                continue

if __name__ == "__main__":
    for tagg in CLEARTAGS:
        nametags(tagg)
        print('entering nametags')
    metatags(CLEARTAGS)
    print('entering metatags')
    for ff in FILES:
        print('entering run')
        run(ff, CLEARTAGS)
