#!/usr/bin/python3
"""Function that reads a text file and prints it to stdout"""


def read_file(filename=""):
    """Opens file and prints it"""

    with open(filename, 'r', encoding='utf-8') as myFile:
        print(myFile.read(). end='')
