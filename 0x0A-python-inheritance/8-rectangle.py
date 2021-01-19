#!/usr/bin/python3
"""Write an empty class"""


class BaseGeometry:
    """New class"""

    pass

    def area(self):
        """public instance method"""

        raise Exception(" area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""

        if type(value) != int:
            raise TypeError('<name> must be an integer')

        elif value <= 0:
            raise TypeError('<name> must be greater than 0')

class Rectangle(BaseGeometry):
    """New sub class"""

    def __init__(self, width, height):
        """Instantiation with width and height private"""

        self.__width__ = width
        self.__height__ = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
