#!/usr/bin/python3
"""Write a class that defines a rectangle"""


class Rectangle:
    """Empty class"""

    def __init__(self, width=0, height=0):
        """Instantiation of rectangle"""
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__ (self):
        """To print the rectangle with the # character"""
        str = ""
        if (self.__width != 0 and self.__height != 0):
            str = "\n".join(["#" * self.__width] * self.__height)
        return str
