#!/usr/bin/python3
"""class call it Square"""


class Square:
    """class call it Square"""

    def __init__(self, size=0, position=(0, 0)):
        """size is a private attribute"""
        self.size = size
        self.position = position
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """size is a private attribute"""
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        if self.__size != 0:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end='')
                for j in range(self.__size):
                    print("#", end='')
                print()
        else:
            print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if len(value) is not 2 or type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(h) is not int for h in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if self.__position[0] < 0 or self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
