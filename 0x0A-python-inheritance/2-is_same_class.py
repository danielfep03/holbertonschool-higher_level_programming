#!/usr/bin/python3
''' Module to learn how type() works '''


def is_same_class(obj, a_class):
    ''' Check if obj is exactly an instance of a_class '''
    if type(obj) is a_class:
        return True
    return False
