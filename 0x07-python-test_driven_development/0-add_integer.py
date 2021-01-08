#!/usr/bin/python3
''' Project for studying doctests in python '''


def add_integer(a, b=98):
    ''' Function that Adds 2 integer '''

    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not float:
        raise TypeError("b must be an integer")
    return a + b
