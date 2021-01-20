#!/usr/bin/python3
''' Code to learn to use issubclass()'''

def inherits_from(obj, a_class):
    ''' Check if the object is an instance of a class '''
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
       return True
    return False
