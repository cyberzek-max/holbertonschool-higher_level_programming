#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_ = []
    for i in my_list:
        if i == search:
            list_ += [replace]
        elif i =  replace:
            list_ += [search]
        else:
            list_ += [i]
    return list_
