#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    list_ = []
    for i in set_1:
        for x in set_2:
            if i == x:
                list_ += [i]
    list_1 = []
    for i in list(set_1) + list(set_2):
        if i not in list_ and i not in list_1:
            list_1 += [i]
    return list_1
