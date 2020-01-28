#!/usr/bin/python3
"""Module for Base class."""

import json


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base"""
        if id is not None:
            self.id = id

        else:

            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the representation of a str to json"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """returns the representation json to str"""
        obj = []
        if list_objs is None:
            obj = []
        else:
            obj = [x.to_dictionary() for x in list_objs]
        obj = cls.to_json_string(obj)
        fl = cls.__name__ + ".json"
        with open(fl, "w") as f:
            f.write(obj)

    def from_json_string(json_string):
        """returns the list represented by json-sting"""
        ls = []
        if json_string is None:
            return ls
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """class method crate"""
        if cls.__name__ == "Square":
            dummy = cls(4)
            dummy.update(**dictionary)
            return dummy

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 4)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """load from file func"""
        fl = cls.__name__ + "json"
        ls = []
        try:
            txt = []
            with open(fl, 'r') as f:
                txt = cls.from_json_string(f.read())
                for tmp in txt:
                    ls.append(cls.create(**tmp))
        except:
            pass
        return ls
