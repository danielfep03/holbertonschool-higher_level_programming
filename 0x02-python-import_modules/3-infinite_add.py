#!/usr/bin/python3
import sys
if __name__ == "__main__":
    result = 0
    argc = len(sys.argv)
    for i in range(1, argc):
        number = int(sys.argv[i])
        result += number
    print("{}".format(result))
