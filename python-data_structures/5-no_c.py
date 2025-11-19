#!/usr/bin/python3
def no_c(my_string):
    x=""
    for i in my_string:
        if i!="c" or i!="C":
            x+=i
    return x
