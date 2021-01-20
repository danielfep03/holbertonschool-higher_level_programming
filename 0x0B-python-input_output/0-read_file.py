#!/usr/bin/python3
'''  Code to lear to read a file '''


def read_file(filename=""):
    ''' Read filename '''
    with open(filename) as f:
        for line in f:
            print(line, end='')
    print()
