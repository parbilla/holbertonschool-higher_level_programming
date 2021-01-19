#!/usr/bin/python3
"""Module of geometry"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


"""Program create a rectangle"""


class Rectangle(BaseGeometry):
    """Class Rectangle inherited of base geometry"""

    def __init__(self, width, height):
        """Constructor method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
