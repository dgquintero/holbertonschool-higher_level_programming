#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) is 0:
        return None
    _max = my_list[0]
    for item in my_list:
        if item > _max:
            _max = item
    return _max
