#!/usr/bin/python3
"""Module that has the function say_my_name that prints a name"""


def say_my_name(first_name, last_name=""):
    """Function that prints to strings with name and a surname.
If the varables are not strings raise a TypeError"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name name must be a string")

    print("My name is {} {}".format(first_name, last_name))
