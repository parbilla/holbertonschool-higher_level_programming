#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        """set value"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ get value """

        return self.__height

    @height.setter
    def height(self, height):
        """set value"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
         """ get value """
         return self.__x

    @x.setter
    def x(self, x):
        """set value"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ get value """
        return self.__y

    @y.setter
    def y(self, y):
        """set value"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("x must be >= 0")
        self.__y = y

    def area(self):
        """area of rectangle"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        print('\n' * self.__y, end='')

        for i in range(self.height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        """Update the class Rectangle by overriding the __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}" .format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assign an argument to each attribute"""
        rectangle_attrs = ["id", "width", "height", "x", "y"]
        if args is None or len(args) == 0:
            for k, v in kwargs.items():
                if k in rectangle_attrs:
                    setattr(self, k, v)
        else:
            for i in range (len(args)):
                setattr(self, rectangle_attrs[i], args[i])

    def to_dictionary(self):
        """return a dictionary of Rectangle"""
        rectangle_dict = {'id': self.id, 'width': self.__width,
                       'height': self.__height, 'x': self.__x, 'y': self.__y}
        return rectangle_dict
