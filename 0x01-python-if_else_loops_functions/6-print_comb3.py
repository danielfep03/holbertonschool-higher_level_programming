#!/usr/bin/python3
y = 0
for i in range(0, 10):
    y = y + 1
    x = 0
    for x in range(x + y, 10):
        print("{:d}".format(i), end='')
        if i != 8 or x != 9:
            print("{:d}, ".format(x), end='')
        else:
            print("{:d}".format(x))
