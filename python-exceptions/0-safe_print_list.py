#!/usr/bin/python3


def lenim(x):
    k = 0
    for _ in x:
        k += 1
    return k


def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    print()
    return count
