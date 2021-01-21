#!/usr/bin/python3
"""Write a class that inherits from int"""


class MyInt(int):
    """New class"""

    def __init__(self, num):
        """Init number"""
        self.__num = num

    def __eq__(self, num):
        """Compare equality"""
        return False

    def __ne__(self, num):
        """Compare inequality"""
        return True
