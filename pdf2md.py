#!/usr/bin/python

import PyPDF2
import re
from io import BytesIO
import argparse
import os

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Extract text from PDFs and format it into Markdown.')

# Add command-line arguments
parser.add_argument('--input_dir', required=True, help='Directory containing PDF files to process')
parser.add_argument('--output_dir', required=True, help='Output directory for Markdown files')

# Parse the command-line arguments
args = parser.parse_args()

print(args.output_dir)

# Ensure output directory exists
os.makedirs(args.output_dir, exist_ok=True)

# Iterate through PDF files in the input directory
for pdf_file in os.listdir(args.input_dir):
    if pdf_file.lower().endswith('.pdf'):
        pdf_path = os.path.join(args.input_dir, pdf_file)

        # Open and Extract PDF Text
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            pdf_text = ''
            for page_num in range(len(pdf_reader.pages)):
                pdf_text += pdf_reader.pages[page_num].extract_text()

        # Rest of the code remains the same...

        # Create and Write to Markdown File
        markdown_file_name = os.path.splitext(pdf_path)[0] + '.md'
        markdown_file_path = os.path.join(args.output_dir, markdown_file_name)
        with open(markdown_file_path, 'w', encoding="utf-8") as markdown_file:
            markdown_file.write(pdf_text)
