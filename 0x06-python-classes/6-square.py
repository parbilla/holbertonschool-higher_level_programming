#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """New class"""
    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with size and position"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Conditions of position value"""
        if type(value) is not tuple or len(value) != 2 or value[0] is not int \
           or value[1] is not int or value[0] <= 0 or value[1] <= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Method that returns current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Method that prints the square with #"""
        if self.__size > 0:
            for k in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end='')
                print("#" * self.__size)
        else:
            print()
