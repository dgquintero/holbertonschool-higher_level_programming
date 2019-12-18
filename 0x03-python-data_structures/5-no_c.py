#!/usr/bin/python3
def no_c(my_string):
    new_s = ""
    for tmp in my_string:
        if tmp == 'c' or tmp == 'C':
            continue
        new_s = new_s + tmp
    return new_s
