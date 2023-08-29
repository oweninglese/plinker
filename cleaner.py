#!usr/bin/python

# CLeanup

import argparse
import re

parser = argparse.ArgumentParser(description=' Clean Markdown.')

parser.add_argument('--files', nargs='+', required=True, help='Single File')
args = parser.parse_args()


def cleaner(file):
    """
    Cleans the text in the given file.

    Args:
        file (str): The path to the file to be cleaned.

    Returns:
        None
    """
    with open(file, "r", encoding="utf-8") as fiel:
        text = fiel.read()

        # Clcleaned_text
        cleaned_text = re.sub(r'\s+', ' ', text)
        cleaned_text = re.sub(r'\s+', ' ', text)

        # Remove footnotes and references (assuming they are enclosed in square brackets)
        cleaned_text = re.sub(r'\[.*?\]', '', cleaned_text)

        # Remove entire footnotes (including their content)
        cleaned_text = re.sub(r'\[\d+\].*?(?=\s*\[\d+\]|\Z)', '', cleaned_text, flags=re.DOTALL)

        # Identify headings and format them
        headings = re.findall(r'(?:\n|^)([A-Z][A-Z0-9\s]+)\n', cleaned_text)
        for heading in headings:
            cleaned_text = cleaned_text.replace(heading, f"\n# {heading}\n")

        # Replace bullet points
        cleaned_text = cleaned_text.replace('- ', '- ')

        # Replace inline formatting
        cleaned_text = re.sub(r'\*\*(.*?)\*\*', r'**\1**', cleaned_text)  # Bold
        cleaned_text = re.sub(r'\*(.*?)\*', r'*\1*', cleaned_text)        # Italics

        # Replace inline formatting
        cleaned_text = re.sub(r'\*\*(.*?)\*\*', r'**\1**', cleaned_text)  # Bold
        cleaned_text = re.sub(r'\*(.*?)\*', r'*\1*', cleaned_text)        # Italics

        # Remove page numbers or headers/footers
        cleaned_text = re.sub(r'\d+', '', cleaned_text)  # Remove numbers
        cleaned_text = re.sub(r'Page \d+', '', cleaned_text)  # Remove "Page X"

        # Break text into chunks of five sentences each with a line break
        sentences = re.split(r'(?<=[.!?]) +', cleaned_text)
        chunk_size = 5
        text_chunks = [sentences[i:i+chunk_size] for i in range(0, len(sentences), chunk_size)]
    with open(file, "w", encoding="utf-8") as fiel:
        for chunk in text_chunks:
            fiel.write(" ".join(chunk) + "\n")

if __name__ == "__main__":
    FILES = args.files
    for FILE in FILES:
        if FILE.endswith('.md'):
            cleaner(FILE)
