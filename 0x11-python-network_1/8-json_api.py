#!/usr/bin/python3
'''
Module that sends a Post equest with a lleter as parameter
'''
import requests
from sys import argv


def main():
    if len(argv) == 1 or argv[1].isdigit():
        print('No result')
    else:
        r = requests.post('http://0.0.0.0:5000/search_user',
                          data={'q': argv[1]})
        k = r.json()
        print('[{}] {}'.format(k.get('id'), k.get('name')))

if __name__ == "__main__":
    main()
