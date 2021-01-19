#!/usr/bin/python3
"""Returns if object is an instance of a class inherited from"""
""" the specified class"""


def inherits_from(obj, a_class):
    """True if it inherited from a class"""

    if issubclass(type(obj), a_class):
        if type(obj) != a_class:
            return True
    return False
