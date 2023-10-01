#!/usr/bin/python3
"""
This module contains a class Square that inherits from Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that represents a square.
    """
    def __init__(self, size):
        """
        Initializes a new Square object with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """
        Returns a string representation of the square in the
        format [Rectangle] <size>/<size>.

        Returns:
            A string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def __repr__(self):
        """
        Returns a string representation of the square that can be used
        to recreate the object.

        Returns:
            A string representation of the square.
        """
        return "Square({})".format(self.__size)
