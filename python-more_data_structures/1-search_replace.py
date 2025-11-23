#!/usr/bin/python3
l = []
def search_replace(my_list, search, replace):
    for i in my_list:
        if i == search:
            l += [replace]
        elif i == replace:
            l += [search]
        else:
            l += [i]
    return l
