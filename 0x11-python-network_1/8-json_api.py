#!/usr/bin/python3
'''
Module that sends a Post equest with a lleter as parameter
'''
import requests
from sys import argv

if __name__ == "__main__":
    values = {'q': ""}
    if len(argv) == 2:
        values['q'] = argv[1]
        r = requests.post('http://0.0.0.0:5000/search_user',
                          data={'q': argv[1]})
    else:
        
            r = requests.post('http://0.0.0.0:5000/search_user',
                              data={'q': argv[1]})
    try:
            k = r.json()
            if k:
                print('[{}] {}'.format(k.get('id'), k.get('name')))
            else:
                print('No result')
    except:
        print('Not a valid Json')
