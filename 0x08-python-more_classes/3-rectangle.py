#!/usr/bin/python3
"""class call it Rectangle"""


class Rectangle:
    """class call it Rectangle"""

    def __init__(self, width=0, height=0):
        """width and height are private attribute"""
        self.__width = width
        self.__height = height
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return(self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.__width + self.__height)

    def __str__(self):

        if self.__width == "0" or self.__height == "0":
            return ""
        str_rep = ""
        for i in range(self.__height):
            for j in range(self.__width):
                str_rep += "#"
            if i is not self.__height - 1:
                str_rep += "\n"
        return str_rep
