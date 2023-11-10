#!/usr/bin/python3
"""Deines a base Model class"""
import json


class Base:
    """Represents a base odel"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """A"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        file_name = cls.__name__ + ".json"
        with open(file_name, 'w') as jsf:
            if list_objs is None:
                jsf.write("[]")
            else:
                dictionary_list = [m.to_dictionary() for m in list_objs]
                jsf.write(Base.to_json_string(dictionary_list))
