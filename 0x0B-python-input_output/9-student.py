#!/usr/bin/python3
"""Function that Write a class Student that defines a student"""


class Student:
    """Public instance attributes"""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first name, last name, age"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation of a Student instance"""

        return self.__dict__
