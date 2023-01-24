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

    def area(self):
            """Return the square area"""
            return (self.__size * self.__size)
