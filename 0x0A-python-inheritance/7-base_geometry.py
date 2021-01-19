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
            raise TypeError('{} must be an integer'.format(name))

        elif value <= 0:
            raise TypeError('{} must be greater than 0'.format(name))
