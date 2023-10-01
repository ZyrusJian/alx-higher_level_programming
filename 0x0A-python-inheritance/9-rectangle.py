#!/usr/bin/python3
"""
This module contains a class Rectangle that inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class that represents a rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes a new Rectangle object with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle in the
        format [Rectangle] <width>/<height>.

        Returns:
            A string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def __repr__(self):
        """
        Returns a string representation of the rectangle that can be
        used to recreate the object.

        Returns:
            A string representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
