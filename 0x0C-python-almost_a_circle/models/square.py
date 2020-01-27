#!/usr/bin/python3
"""Module for Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """property for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """return the str representation of square"""
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                                                  self.x,
                                                  self.y,
                                                  self.width))

    def update(self, *args, **kwargs):
        """Update the class square"""
        if args:
            for idx, value in enumerate(args):
                if idx == 0:
                    self.id = value
                elif idx == 1:
                    self.size = value
                elif idx == 2:
                    self.x = value
                elif idx == 3:
                    self.y = value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns a dictionary with the representation of square"""
        dictionary = {'id': self.id,
                      'size': self.size,
                      'x': self.x,
                      'y': self.y}
        return dictionary
