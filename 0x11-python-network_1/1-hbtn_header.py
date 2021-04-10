#!/usr/bin/python3
''' Script that displays the value of the X-Request-Id variable'''

from urllib import request
import sys

if __name__ == '__main__':
    with request.urlopen(sys.argv[1]) as response:
        body = response.info()
    print(body.get('X-Request-Id'))
