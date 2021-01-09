#!/usr/bin/python3
''' Project for studying doctest in python '''


def text_indentation(text):
    '''Prints a text with 2 new lines after each of these characters'''
    if type(text) is not str:
        raise TypeError("text must be a string")

    string = text.strip(" ")

    for i in range(len(string)):
        if string[i - 1] in ('?', ':', '.') and string[i] == ' ':
            continue
        print(string[i], end='')
        if string[i] in ('?', ':', '.'):
            print("\n")
