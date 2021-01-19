#!/usr/bin/python3
"""Returns if the object is an instance of,"""
""" or if it is an instance of a class that inherited from"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of, otherwise False"""

    if isinstance(obj, a_class) or issubclass(type(obj), a_class):
        return True
    else:
        return False
