#!/usr/bin/python3
"""Define a square"""


class Square:
    """Represent a new square"""
    def __init__(self, size=0):
            """Initialize a new square.
            Args:
            size (int): instance attribute"""
            if not isinstance(size, int):
                 raise TypeError("size must be an integer")
            elif size < 0:
                 raise ValueError("size must be >= 0")
            self.__size = size

    @property
    def size(self):
            return self.__size

    @size.setter
    def size(self, value):
            self.__size = value
    if not isinstance(value, int):
            raise TypeError("size must be an integer")
    elif value < 0:
            raise ValueError("size must be >= 0")
    return (value)

    def area(self):
            """Return the square area"""
            return (self.__size * self.__size)
