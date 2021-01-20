#!/usr/bin/python3
''' Code to learn how to append into a file '''


def append_write(filename="", text=""):
    ''' Append into filename the text '''
    with open(filename, "a") as f:
        f.write(text)
    return len(text)
