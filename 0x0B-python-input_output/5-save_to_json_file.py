#!/usr/bin/python3
"""
This module contains a function that writes an Object to a text file,
using a JSON representation.
"""


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj (object): The object to write to the file.
        filename (str): The name of the file to write to.
    """
    import json
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
