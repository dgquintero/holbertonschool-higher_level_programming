#!/usr/bin/python3
def uppercase(str):
    for tmp in str:
        if ord(tmp) >= 97 and ord(tmp) <= 122:
            tmp = chr(ord(tmp) - 32)
        print("{:s}".format(tmp), end="")
    print("")
