#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        c = 0
        for i in range(x):
            print("{}".format(my_list[i]), end='')
            c += 1
        print()
        return (c)
    except IndexError:
        print()
        return (c)
