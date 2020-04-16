#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
"""

import urllib.parse as parse
import urllib.request as request
from sys import argv


if __name__ == "__main__":
    values = {'email': argv[2]}
    data = parse.urlencode(values).encode('ascii')
    r = request.Request(argv[1], data)
    with request.urlopen(r) as re:
        print(re.read().decode('utf-8'))
