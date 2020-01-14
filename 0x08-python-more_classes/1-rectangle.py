#!/usr/bin/python3
"""class call it Rectangle"""


class Rectangle:
    """class call it Rectangle"""

    def __init__(self, width=0, height=0):
        """width and height are private attribute"""
        self.__width = width
        self.__height = height
        """if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("size must be >= 0")

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @height.setter
    def height(self, value):
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
