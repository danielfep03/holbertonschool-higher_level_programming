#!/usr/bin/python3
''' Module to create aobject from a Json file '''

import json


def load_from_json_file(filename):
    '''function that creates an Object from a JSON file '''
    with open(filename, 'r') as f:
        return json.loads(f.read())
