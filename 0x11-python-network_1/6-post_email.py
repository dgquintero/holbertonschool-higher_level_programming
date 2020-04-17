#!/usr/bin/python3
''' Python script that fetches https://intranet.hbtn.io/status
must use the package requests
'''
import requests
from sys import argv


if __name__ == "__main__":
    values = {'email': argv[2]}
    r = requests.post(argv[1], data=values)
    print(r.text)
