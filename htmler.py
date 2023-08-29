#!/bin/python

""" Markdown to HTML
"""
import os
import subprocess
# import md_to_html as to_html


def convert_md_to_html(input_md_file, output_file):
    """Convert Markdown file to HTML

    Args:
        input_md_file (.md): markdown file
        output_html_file (.html): html file
    """
    try:
        # Run the md-to-html command as a subprocess
        subprocess.run(
            ["md-to-html", "-i", input_md_file, "-o", output_file], check=True
        )
        print(
            f"Markdown to HTML conversion successful."
            f"HTML file saved to: {output_file}"
        )
    except subprocess.CalledProcessError as error:
        print(f"Error converting Markdown to HTML: {error}")


if __name__ == "__main__":
    FOLDER_PATH = (
        "/home/ofoo/Dev/md_project/arts_copy/"
        # Replace this with the path to your folder
    )
    HTML = os.path.join(FOLDER_PATH, "html")
    # Process each file in the folder
    for file_name in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH, file_name)

        # Skip directories, process only files
        if not os.path.isfile(file_path):
            continue

        # Check if the file has a ".md" extension
        if file_path.lower().endswith(".md"):
            # Generate the output HTML file path
            # by replacing ".md" with ".html"
            output_html_file = os.path.join(HTML, file_name[:-3] + ".html")
            convert_md_to_html(file_path, output_html_file)
