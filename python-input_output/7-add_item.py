#!/usr/bin/python3

"""
add new argument to python list
"""

import json
import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
newlist = []
for i in range(1, len(sys.argv)):
    load_from_json_file(filename)
    newlist.append(sys.argv[1:])
    save_to_json_file(newlist, filename)
