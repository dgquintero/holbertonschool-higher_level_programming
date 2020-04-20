#!/usr/bin/python3
'''
Module that sends a Post request with a lleter as parameter
'''

import requests
from sys import argv


if __name__ == "__main__":
    values = {'q': ""}
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) == 2:
        word_passed = argv[1]
        values['q'] = word_passed
        r = requests.post(url, data=values)
    else:
        r = requests.post(url, data=values)
    try:
        k = r.json()
        if k:
            print('[{}] {}'.format(k.get('id'), k.get('name')))
        else:
            print('No result')
    except:
        print('Not a valid JSON')
