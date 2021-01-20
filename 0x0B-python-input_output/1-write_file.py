#!/usr/bin/python3
''' Code to learn how to write into a file '''


def write_file(filename="", text=""):
    ''' Write into filename the text '''
    with open(filename, "w") as f:
        f.write(text)
    return len(text)
