#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) in range(97, 123):
            char = chr(ord(char) - 32)
        print("{:s}".format(char), end='')
    print("\n", end='')
