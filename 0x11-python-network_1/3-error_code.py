#!/usr/bin/python3
''' Script that displays the body of the response '''

from urllib import request
from sys import argv
from urllib.error import HTTPError

url = argv[1]

if __name__ == '__main__':
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('UTF-8'))
    except HTTPError as err:
        print('Error code: {}'.format(err.code))
