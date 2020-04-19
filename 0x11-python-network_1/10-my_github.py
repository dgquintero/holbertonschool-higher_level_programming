#!/usr/bin/python3
''' Write a Python script that takes your Github credentials 
(username and password) and uses the Github API to display your id
'''
import requests
from sys import argv
def main():
    r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
