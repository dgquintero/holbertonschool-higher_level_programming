#!/usr/bin/python3


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None)
        if attrs is None:
            return self.__dict__
        _dict = {}
        for i in attrs:
            try:
                _dict[i] = self.__dict__
            except:
                pass
        return _dict
