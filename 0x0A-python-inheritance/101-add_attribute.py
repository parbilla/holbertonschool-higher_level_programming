#!/usr/bin/python3
"""Write a function that adds a new attribute to an object if its possible"""


def add_attribute(obj, name, value):
    """add attribute to object"""
    if hasattr(obj, name):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
