#!/usr/bin/python3
"""Function that appends a string at the end of a text file """
"""and returns the number of characters added"""


def append_write(filename="", text=""):
    """Append text in file"""

    with open(filename, mode='a', encoding='utf-8') as myFile:
        return myFile.write(text)
