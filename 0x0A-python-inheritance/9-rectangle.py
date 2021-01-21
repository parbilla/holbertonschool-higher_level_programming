#!/usr/bin/python3
"""Write a class that inherits from BaseGeometry"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


"""Program create a rectangle"""


class Rectangle(BaseGeometry):
    """Class Rectangle inherited of BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Area method implemented"""
        return self.__width * self.__height

    def __str__(self):
        """String method"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
