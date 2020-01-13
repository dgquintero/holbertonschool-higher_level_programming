#!/usr/bin/python3
"""Module that has the function text_indentation"""


def text_indentation(text):
"""Function that prints a text indented. If the function found a this special
 characters ":" or  "." or "?" puts a new line in the text"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    sentinel = 0
    for i in text:
        if sentinel == 0:
            if i == ' ':
                continue
            else:
                sentinel = 1
        if sentinel == 1:

            if i == "." or i == ":" or i == "?":
                print(i)
                print()
                sentinel = 0
            else:
                print(i, end="")
