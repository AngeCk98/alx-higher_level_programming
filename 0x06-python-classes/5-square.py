#!/usr/bin/python3
"""Define a square"""


class Square:
    """Represent a new square"""
    def __init__(self, size=0):
        """Initialize a new square.
        Args:
        size (int): instance attribute"""
        self.__size = size

    @property
    def size(self):
        """Gets the value of private attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Changes value of private attribute size
        Args:
            value (int): new value of size"""
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        return (value)

     def area(self):
            """Return the square area"""
            return (self.__size * self.__size)

        def my_print(self):
            """Print square as '#'"""
            for i in range(0, self.__size):
                [print("#", end="") for j in range(self.__size)]
                print()
            if self.__size == 0:
                print()

