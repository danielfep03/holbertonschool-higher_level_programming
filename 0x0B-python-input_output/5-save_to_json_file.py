#!/usr/bin/python3
''' Code to learn how to write an object to a text file using Json'''


import json


def save_to_json_file(my_obj, filename):
    ''' Writes an Object to a text file, using a JSON representation '''
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
