#!/usr/bin/python3
"""Deines a base Model class"""
import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        """A"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        instance = cls(1, 1, 1, 1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as f:
                list_dicts = Base.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = f"{cls.__name__}.csv"

        with open(filename, "w", newline="") as csvfile:
            fieldnames = ["id", "width", "height", "x", "y"]
            \if cls.__name__ == "Rectangle" else ["id", "size", "x", "y"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if list_objs:
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
            else:
                csvfile.write("[]")

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = f"{cls.__name__}.csv"

        try:
            with open(filename, "r", newline="") as csvfile:
                fieldnames = ["id", "width", "height", "x", "y"]
                \if cls.__name__ == "Rectangle" else ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []