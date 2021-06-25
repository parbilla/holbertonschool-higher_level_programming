#!/usr/bin/python3
class LockedClass:
    """Only instances a new attribute if it is called first_name"""
		__slots__="first_name"
		