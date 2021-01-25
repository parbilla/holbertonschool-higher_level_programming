#!/usr/bin/python3
import json

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + '.json'
        myList = []
        with open(filename, mode='w', encoding='utf-8') as myFile:
            if list_objs is None:
                myFile.write(cls.to_json_string(myList))
            else:
                for obj in list_objs:
                    myList.append(obj.to_dictionary())
                myFile.write(cls.to_json_string(myList))
