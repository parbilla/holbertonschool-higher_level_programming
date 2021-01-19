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
