#!/usr/bin/python3
""" a script that adds all arguments to a Python list,
    and then save them to a file:
"""

import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

stdin_arg = sys.argv[1:]
filename = "add_item.json"
argument = []

try:
    argument = load_from_json_file(filename)
except Exception:
    argument = []

for items in stdin_arg:
    argument.append(items)
save_to_json_file(argument, filename)
