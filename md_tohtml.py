#!/bin/python

""" Markdown to HTML
"""
import os
import subprocess


def convert_md_to_html(input_md_file, output_html_file):
    """ Convert Markdown file to HTML

    Args:
        input_md_file (.md): markdown file
        output_html_file (.html): html file
    """    
    try:
        # Run the md-to-html command as a subprocess
        subprocess.run(['md-to-html', input_md_file, '-o', output_html_file], check=True)
        print(f"Markdown to HTML conversion successful. HTML file saved to: {output_html_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error converting Markdown to HTML: {e}")


if __name__ == "__main__":
    FOLDER_PATH = "/home/ofoo/Docs/proj/arts/"  # Replace this with the path to your folder

    # Process each file in the folder
    for file_name in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH, file_name)

        # Skip directories, process only files
        if not os.path.isfile(file_path):
            continue

        # Check if the file has a ".md" extension
        if file_path.lower().endswith(".md"):
            # Generate the output HTML file path by replacing ".md" with ".html"
            output_html_file = file_path[:-3] + ".html"
            convert_md_to_html(file_path, output_html_file)
