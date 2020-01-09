#!/usr/bin/python3

"""class call it Square"""
class Square:
    """class call it Square"""
    def __init__(self, size):
        """size is a private attribute"""
        if type (size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
