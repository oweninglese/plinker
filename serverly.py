#!/bin/python

from flask import Flask, send_file, render_template, request
import os


app = Flask(__name__)


# Set the path to the folder containing the files to serve
FOLDER_PATH = "/home/ofoo/Docs/proj/arts/html"

FILES = {}
for file_name in os.listdir(FOLDER_PATH):
    FILES[file_name] = FOLDER_PATH + file_name


@app.route('/')
def index():
    """index.html

    Returns:
        html: main page index.html
    """
    return render_template("index.html", files=FILES)


@app.route('/src/<filename>')
def serve_file(filename):
    """Get the full path to the requested file"""
    file_path = os.path.join(FOLDER_PATH, filename)

    # Check if the file exists
    if not os.path.isfile(file_path):
        return "File not found!", 404

    # Send the file to the client
    return send_file(file_path)


if __name__ == "__main__":
    FOLDER_PATH = "/home/ofoo/Dev/arts_copy/html"

    app.run(debug=True)
