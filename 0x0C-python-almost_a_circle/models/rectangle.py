#!/usr/bin/python3
"""Write the class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """New class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get value"""
        return self.__width

    @width.setter
    def width(self, width):
        """Set value"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Get value"""
        return self.__height

    @height.setter
    def height(self, height):
        """Set value"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Get value"""
        return self.__x

    @x.setter
    def x(self, x):
        """Set value"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Get value """
        return self.__y

    @y.setter
    def y(self, y):
        """Set value"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Get area of rectangle"""
        return self.width * self.height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        print('\n' * self.__y, end='')

        for i in range(self.height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        """Update the class Rectangle by overriding the __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}" .format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assign an argument to each attribute"""
        rectangle_attrs = ["id", "width", "height", "x", "y"]
        if args is None or len(args) == 0:
            for k, v in kwargs.items():
                if k in rectangle_attrs:
                    setattr(self, k, v)
        else:
            for i in range(len(args)):
                setattr(self, rectangle_attrs[i], args[i])

    def to_dictionary(self):
        """Return a dictionary of Rectangle"""
        rectangle_dict = {'id': self.id, 'width': self.__width,
                          'height': self.__height, 'x': self.__x,
                          'y': self.__y}
        return rectangle_dict
