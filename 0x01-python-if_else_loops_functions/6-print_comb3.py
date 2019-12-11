#!/usr/bin/python3
for i in range(90):
    if (i != 89):
        if ((i / 10) < (i % 10)):
            print("{:d}{:d}".format(int(i / 10), int(i % 10)), end=", ")
    else:
        print(i)
