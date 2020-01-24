#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                                                    self.x,
                                                    self.y,
                                                    self.__size))
    def update(self, *args, **kwargs):
        if args and args is not None:
            for idx, value in enumerate(args):
                if idx == 0:
                    self.id = value
                elif idx == 1:
                    self.__size = value
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
        dictionary = {'id': self.id,
                      'size': self.size,
                      'x': self.x,
                      'y': self.y}
        return dictionary
