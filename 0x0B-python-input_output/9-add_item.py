#!/usr/bin/python3
from sys import argv


save_to_json = __import__('7-save_to_json_file').save_to_json_file
load_from_json = __import__('8-load_from_json_file').load_from_json_file

filename = 'add_item.json'

try:
    c = load_from_json(filename)
except:
    c = []

for i in argv[1:]:
    c.append(i)
save_to_json(c, filename)
