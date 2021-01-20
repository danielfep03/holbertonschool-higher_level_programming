#!/usr/bin/python3
'''  Code to learn how to read a file '''


def read_file(filename="", encoding='UTF-8'):
    ''' Read filename '''
    with open(filename) as f:
        for line in f:
            print(line, end='')
    print()
