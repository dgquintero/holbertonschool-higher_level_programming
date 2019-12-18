#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    tmp = my_list[:]
    if idx >= len(my_list) or idx < 0:
            return my_list
    tmp[idx] = element
    return tmp
