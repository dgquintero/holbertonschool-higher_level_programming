#!/usr/bin/python3
"""Module for Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """property for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """property for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """property for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        self.__x = value
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """property for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        self.__y = value
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """Method that returns the area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """print in stdo the rectangle"""

        for i in range(self.__y):
            print("\n", end='')
        for j in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width)

    def __str__(self):
        """return the str representation of rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.__x,
                                                        self.__y,
                                                        self.__width,
                                                        self.__height))

    def update(self, *args, **kwargs):
        """Update the class rectangle"""
        if args and args is not None:
            for idx, value in enumerate(args):
                if idx == 0:
                    self.id = value
                elif idx == 1:
                    self.__width = value
                elif idx == 2:
                    self.__height = value
                elif idx == 3:
                    self.__x = value
                elif idx == 4:
                    self.__y = value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns a dictionary with the representation of rectangle"""
        dictionary = {'id': self.id,
                      'width': self.width,
                      'height': self.height,
                      'x': self.x,
                      'y': self.y}
        return dictionary
