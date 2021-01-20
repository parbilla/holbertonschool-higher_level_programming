#!/usr/bin/python3
"""Function that writes an Object to text file, using a JSON representation """


import json

def save_to_json_file(my_obj, filename):
    """writes to a text file"""

    with open(filename, mode='w', encoding='utf-8') as myFile:
        myFile.write(json.dumps(my_obj))
