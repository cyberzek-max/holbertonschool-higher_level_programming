#!/usr/bin/python3
def print_last_digit(number):
    last = int(str(abs(number))[-1])
    print(last, end="")
    return last
