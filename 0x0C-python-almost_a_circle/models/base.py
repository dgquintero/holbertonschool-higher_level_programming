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
        fl = cls.__name__ + ".json"
        with open(fl, "w") as f:
            json.dump(obj, f)

