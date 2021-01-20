#!/usr/bin/python3
""" Module to learn json"""

from json import JSONEncoder

import json


def from_json_string(my_str):
    ''' Return an object represented by Json string '''
    return json.loads(my_str)
