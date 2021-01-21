#!/usr/bin/python3
''' Add all arguments to a python list, and then save them to a file '''


from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    obj = load_from_json_file(filename)

except FileNotFoundError:
    obj = []

for arg in argv[1:]:
    obj.append(arg)

save_to_json_file(obj, filename)
