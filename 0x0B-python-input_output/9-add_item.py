#!/usr/bin/python3
import sys

save_to_json_file = __import__('7-save_to_json_file.py').save_to_json_file
"""class call it BaseGeometry"""

load_from_json_file = __import__('8-load_from_json_file.py').load_from_json_file

arg = sys.argv[1:]
try:
    c = load_from_json_file("my_add.json")

except IOError:
    c = []

save_to_json_file(a + arg, "my_add.json")
return(save)
