#!/usr/bin/python3
''' Module to create Base class '''


import json


class Base:
    ''' Base class for all modules '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor Method'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' Convert a list to a json string'''
        if list_dictionaries is None or not list_dictionaries:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''Returns the list from the JSON string representation'''

        if json_string is None or json_string[0] is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Save a list of dictionaries to a file'''
        if len(list_objs) <= 1 or list_objs is None:
            new_list = []
        else:
            new_list = []
            for i in list_objs:
                new_list += [i.to_dictionary()]
        my_f = cls.__name__ + ".json"
        with open(my_f, mode='w', encoding='utf-8') as f:
            f.write(cls.to_json_string(new_list))

    @classmethod
    def create(cls, **dictionary):
        '''Returns an instance with all attributes already set'''
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """loads a file"""
        filename = cls.__name__ + ".json"
        data = []
        try:
            with open(filename) as file:
                data = cls.from_json_string(file.read())
            for i, j in enumerate(data):
                data[i] = cls.create(**data[i])
        except:
            pass
        return data
