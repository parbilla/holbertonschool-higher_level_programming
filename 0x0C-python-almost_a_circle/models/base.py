#!/usr/bin/python3
"""Create a base class of all other classes of this project"""
import json
import os


class Base:
    """The goal is to manage id attribute  in all the future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class construtor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + '.json'
        myList = []
        with open(filename, mode='w', encoding='utf-8') as myFile:
            if list_objs is None:
                myFile.write(cls.to_json_string(myList))
            else:
                for obj in list_objs:
                    myList.append(obj.to_dictionary())
                myFile.write(cls.to_json_string(myList))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 2)
        elif cls.__name__ == 'Square':
            dummy = cls(3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        list_instances = []
        filename = cls.__name__ + '.json'
        if os.path.exists(filename) is False:
            return list_instances
        with open(filename, mode='r', encoding='utf-8') as myFile:
            objs = cls.from_json_string(myFile.read())
            for i in objs:
                list_instances.append(cls.create(**i))
            return list_instances
