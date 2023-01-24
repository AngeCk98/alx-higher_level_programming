#!/usr/bin/python3
"""Define a square"""


class Square:
    """Represent a new square"""

    ErrMessage = "position must be a tuple of 2 positive integers"

    def __init__(self, size=0, position=(0, 0)):
            """Initialize a new square.
            Args:
            size (int): The size of the new square
            position (int, int): The position of the new square"""
            self.___size = size
            self.__position = position

    @property
    def size(self):
            """Gets the value of private attribute size"""
            return (self.__size)

    @size.setter
    def size(self, value):
            """Changes value of private attribute size
            Args:
                value (int): new value of size"""
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

            @property
            def position(self):
                """Gets the current position of private attribute size"""
                return (self.__position)

            @position.setter
            def position(self, value):
                """Sets the position of private attribute size
                Args:
                    value (int): new value of size"""
                    if not (isinstance(value, tuple) or
                    len(value) != 2 or
                    not all(isinstance(elem, int) for elem in value) or
                    not all(elem >= 0 for elem in value)):
                    raise TypeError("{}".format(ErrMessage))
            self.__position = value

    def area(self):
            """Return the square area"""
            return (self.__size * self.__size)

    def my_print(self):
            """Print a square with '#' characters"""
            if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
        print("")
