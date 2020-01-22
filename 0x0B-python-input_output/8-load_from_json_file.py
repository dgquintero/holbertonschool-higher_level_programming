#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, mode='r', encoding='utf-8') as f:
        json.load(f)
