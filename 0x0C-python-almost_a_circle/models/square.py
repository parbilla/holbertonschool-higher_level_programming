#!/usr/bin/python3
"""Write the class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """New class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get value"""
        return self.width

    @size.setter
    def size(self, size):
        """Set value"""
        self.width = size
        self.height = size

    def __str__(self):
        """Update the class Square by overriding the __str__ method"""
        return "[Square] ({}) {}/{} - {}" .format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """Assign an argument to each attribute"""
        square_attrs = ["id", "size", "x", "y"]
        if args is None or len(args) == 0:
            for k, v in kwargs.items():
                if k in square_attrs:
                    setattr(self, k, v)
        else:
            for i in range(len(args)):
                setattr(self, square_attrs[i], args[i])

    def to_dictionary(self):
        """Return dictionary with values"""
        square_dict = {'id': self.id, 'size': self.size,
                       'x': self.x, 'y': self.y}
        return square_dict
