#!/usr/bin/python3
sumall = 0
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0")
    else:
        for i in range(1, len(sys.argv)):
            sumall += int(sys.argv[i])
        print("{:d}".format(sumall))
