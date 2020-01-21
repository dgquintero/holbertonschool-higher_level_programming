#!/usr/bin/python3
"""func returns T or F if obj is an instance of a_class"""


def inherits_from(obj, a_class):
    return isinstance(obj, a_class) and type(obj) != a_class
