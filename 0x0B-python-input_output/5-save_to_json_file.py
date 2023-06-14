#!/usr/bin/python3
"""A function that writes an Object to a text file,
    using a JSON representation:
"""

import json


def save_to_json_file(my_obj, filename):
    """Object to a text file, using a JSON represtations"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dumb(my_obj, file)
