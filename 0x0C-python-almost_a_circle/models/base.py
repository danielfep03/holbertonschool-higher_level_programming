#!/usr/bin/python3
''' Module to create Base class '''

import json
class Base:
    ''' Base class for all modules '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None and list_dictionaries[0] is None:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            new_list = []
        else:
            new_list = []
            for items in list_objs:
                new_list.append(cls.to_dictionary(items))
            new_list = Base.to_json_string(new_list)

        with open("{}.json".format(cls.__name__), 'w') as f:
            f.write(new_list)
