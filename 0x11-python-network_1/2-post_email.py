#!/usr/bin/python3
''' Script that sends a POST request and display the body of the response '''

from urllib import request, parse
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    email_dict = {'email': argv[2]}
    email = parse.urlencode(email_dict).encode('ASCII')

    with request.urlopen(url, email) as response:
        print(response.read().decode('UTF-8'))
