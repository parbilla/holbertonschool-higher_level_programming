#!/usr/bin/python3
"""Write a class Square that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square inherited of Rectangle"""

    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Area method implemented"""
        return self.__size ** 2

        def __str__(self):
            """String method"""
            return "[Square] {}/{}".format(self.__size, self.__size)
