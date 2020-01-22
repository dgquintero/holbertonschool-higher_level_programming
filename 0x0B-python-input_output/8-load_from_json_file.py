#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """function that writes an Object to a text file, using a JSON representation"""
    with open(filename, mode='w', encoding='utf-8') as f: 
        json.dump(my_obj, f)
