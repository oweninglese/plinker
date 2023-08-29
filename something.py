#! /usr/bin/python

import PyPDF2
import requests
import re
from io import BytesIO


pdf_reader = PyPDF2.PdfReader(pdf_content)
pdf_text = ''
for page_num in range(len(pdf_reader.pages)):
    pdf_text += pdf_reader.pages[page_num].extract_text()

# Clean up extra spaces and line breaks
cleaned_text = re.sub(r'\s+', ' ', pdf_text)

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

# Remove page numbers or headers/footers
cleaned_text = re.sub(r'\d+', '', cleaned_text)  # Remove numbers
cleaned_text = re.sub(r'Page \d+', '', cleaned_text)  # Remove "Page X"

# Break text into chunks of five sentences each with a line break
sentences = re.split(r'(?<=[.!?]) +', cleaned_text)
chunk_size = 5
text_chunks = [sentences[i:i+chunk_size] for i in range(0, len(sentences), chunk_size)]

# Create and Write to Markdown File
markdown_path = 'output_file.md'
with open(markdown_path, 'w') as markdown_file:
    for chunk in text_chunks:
        markdown_file.write(' '.join(chunk) + '\n\n')
