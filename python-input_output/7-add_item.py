#!/usr/bin/python3

"""
add new argument to python list
"""

import json
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

if filename:
    filee = load_from_json_file(filename)
else:
    filee = []
save_to_json_file(filee + sys.argv[1:], filename)
