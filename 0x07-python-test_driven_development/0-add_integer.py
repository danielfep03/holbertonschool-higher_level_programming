#!/usr/bin/python3
''' Project for studying doctests in python '''


def add_integer(a, b=98):
    ''' Function that Adds 2 integer '''

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a + b)
