#!/usr/bin/python3
"""Print a list , sorted in ascending sort"""


class MyList(list):
    """Write a class that inherits from another"""

    def print_sorted(self):
        """Prints the list sorted by ascending sort"""
        """  if issubclass(MyList, list):"""

        print(sorted(self))
