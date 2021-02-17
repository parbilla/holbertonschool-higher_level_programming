#!/usr/bin/python3
"""Write a class that defines a rectangle"""


class Rectangle:
    """Empty class"""

    def __init__(self, width=0, height=0):
        """Instantiation of rectangle"""
        self.__width = width
        self.__height = height

    def width(self):
        """Get width"""
        return self.__width

    def width(self, value):
        """Set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        """Get height"""
        return self.__height

    def height(self, value):
        """Set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
