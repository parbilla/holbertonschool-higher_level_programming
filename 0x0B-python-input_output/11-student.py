#!/usr/bin/python3
"""Function that writes a class Student that defines a student"""


class Student:
    """Public instance attributes"""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first name, last name, age"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""

        if attrs is None:
            return self.__dict__
        new_dict = {}
        for a in attrs:
            if type(a) is str:
                if i in self_dict__:
                    new_dict[a] = self.__dict__[a]
        return new_dict

        def reload_from_json(self, json):
            """Replaces all attributes of the Student instance"""
            for key in json:
                self.__dict__[key] = json[key]
