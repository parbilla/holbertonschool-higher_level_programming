#!/usr/bin/python3
"""This class has no class or object attribute"""


class LockedClass:
    """Only instances a new attribute if it is called first_name"""
    __slots__ = ["first_name"]
