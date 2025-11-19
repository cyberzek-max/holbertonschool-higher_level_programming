#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    x = argv
    c = 0
    if len(x) == 1:
        print(0)
    else:
        for i in range(1, len(x)):
            c += int(x[i])
        print(c)
