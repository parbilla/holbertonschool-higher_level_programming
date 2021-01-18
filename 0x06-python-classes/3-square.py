#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """New class"""
    def __init__(self, size=0):
        """Instantiation with size"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Method that returns current square area"""
        return self.__size * self.__size
