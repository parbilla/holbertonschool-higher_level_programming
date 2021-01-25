#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        """set value"""
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}" .format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """assign an argument to each attribute"""
        square_attrs = ["id", "size", "x", "y"]
        if args is None or len(args) == 0:
            for k, v in kwargs.items():
                if k in square_attrs:
                    setattr(self, k, v)
        else:
            for i in range (len(args)):
                setattr(self, square_attrs[i], args[i])

    def to_dictionary(self):
        """return dictionary with values"""
        square_dict = {'id': self.id, 'size': self.size,
                       'x': self.x, 'y': self.y}
        return square_dict
