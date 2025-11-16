#!/usr/bin/python3
for n in range(0, 100):
    i = n // 10
    j = n % 10

    if n == 99:
        print("{}{}\n".format(i, j), end="\n")
    else:
        print("{}{}".format(i, j), end=", ")
