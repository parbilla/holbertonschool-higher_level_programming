#!/usr/bin/python3
"""Function that writes a string to a text file """
"""and returns the number of characters written"""


def write_file(filename="", text=""):
    """Write text in file"""

    with open(filename, mode='w', encoding='utf-8') as myFile:
        return myFile.write(text)
