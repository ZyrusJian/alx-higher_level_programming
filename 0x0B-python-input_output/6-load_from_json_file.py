#!/usr/bin/python3
"""
This module contains a function that creates an Object from a “JSON file”.
"""


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        object: The Python data structure represented by
        the JSON string in the file.
    """
    import json
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
