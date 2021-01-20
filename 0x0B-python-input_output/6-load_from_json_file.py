#!/usr/bin/python3
"""Function that creates an Object from a JSON file"""


import json

def load_from_json_file(filename):
    """writes to a text file"""

    with open(filename, encoding='utf-8') as myFile:
        return json.load(myFile)
