#!/usr/bin/python3
"""Returns if the object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """Returns True if is the same class, otherwise False"""

    if type(obj) == a_class:
        return True
    else:
        return False
