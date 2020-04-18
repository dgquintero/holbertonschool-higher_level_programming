#!/usr/bin/python3
''' Python script that fetches https://intranet.hbtn.io/status
must use the package requests
'''
import requests
from sys import argv
def main():
    r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
