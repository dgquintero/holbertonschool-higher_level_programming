#!/usr/bin/python3
''' Write a Python script that takes your Github credentials
(username and password) and uses the Github API to display your id
'''
import requests
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    password = argv[2]
    api = 'https://api.github.com/user'
    r = requests.get(api, auth=(user, password))
    json_dicctionary = r.json()
    print(json_dicctionary.get("id"))
