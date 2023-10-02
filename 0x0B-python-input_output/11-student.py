#!/usr/bin/python3
"""
This module contains a class that defines a student by
public instance attributes and public methods that retrieve and
reload a dictionary representation of a Student instance.
"""


class Student:
    """A class that defines a student by public instance attributes."""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public method that retrieves a dictionary representation of
        a Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    new_dict[attr] = getattr(self, attr)
            return new_dict

    def reload_from_json(self, json):
        """
        Public method that replaces all attributes of
        the Student instance.
        """
        for key, value in json.items():
            setattr(self, key, value)
