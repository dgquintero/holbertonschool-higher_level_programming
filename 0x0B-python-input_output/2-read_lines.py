#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, encoding='utf-8') as f:
        count = 0
        for line in f:
            if (nb_lines <= 0) or (nb_lines >= count):
                print(line, end='')
            count += 1
