#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
"""

import urllib.request as request
import urllib.error as error
from sys import argv


if __name__ == "__main__":
    r = request.Request(argv[1])
    try:
        with request.urlopen(r) as re:
            print(re.read().decode('utf-8'))
    except error.URLError as e:
        print('Error code:', e.code)
