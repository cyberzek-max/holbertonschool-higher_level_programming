#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    return my_list[:idx]+[element]+my_list[idx+1:], my_list[:idx]+[element]+my_list[idx+1:]
