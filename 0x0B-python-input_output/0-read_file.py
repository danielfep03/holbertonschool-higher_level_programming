#!/usr/bin/python3
'''  Code to learn how to read a file '''


def read_file(filename=""):
    ''' Read filename '''
    with open(filename, encoding='UTF-8') as f:
        print(f.read())
