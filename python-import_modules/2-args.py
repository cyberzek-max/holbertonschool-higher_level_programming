#!/usr/bin/python3
from sys import argv
x = argv
if len(x) == 1:
    print("0 arguments.")
elif len(x) == 2:
    print("1 argument:\n1: ", argv[1])
else:
    print("{} arguments:".format(len(x)-1))
    for i in range(1, len(x)):
        print("{}: {}".format(i, argv[i]))
