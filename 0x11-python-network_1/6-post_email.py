#!/usr/bin/python3
'''
Script that sends a POST request to the passed URL
with the email as a parameter
'''

import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    response = requests.post(url, {'email': argv[2]})
    print(response.text)
