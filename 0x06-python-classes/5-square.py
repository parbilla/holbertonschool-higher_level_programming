#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """New class"""
    def __init__(self, size=0):
        """Instantiation with size"""
        self.__size = size

    @property
    def size(self):
        """Retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Conditions of size value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Method that returns current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Method that prints the square with #"""
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
        else:
            print()
