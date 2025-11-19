#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list = my_list[:idx]+[element]+my_list[idx+1:]
    new_list = my_list
    return my_list
