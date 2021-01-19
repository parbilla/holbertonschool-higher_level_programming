#!/usr/bin/python3
"""Write a class that inherits from BaseGeometry"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""New class"""


class Rectangle(BaseGeometry):
    """New sub class"""

    def __init__(self, width, height):
        """Instantiation with width and height private"""

        self.__width__ = width
        self.__height__ = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
