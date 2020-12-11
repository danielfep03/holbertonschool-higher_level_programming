#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argc = len(sys.argv)
    if argc == 2:
        print("{} argument:".format(argc - 1))
        print("1:", sys.argv[1])
    elif argc != 1:
        print("{} arguments:".format(argc - 1))
        for i in range(1, argc):
            print("{}:".format(i), sys.argv[i])
    else:
        print("0 arguments.")
