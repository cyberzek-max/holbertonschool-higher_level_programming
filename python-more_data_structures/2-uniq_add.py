#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_ = []
    for i in my_list:
        if i not in list_:
            list_ += [i]
    summa = 0
    for i in list_:
        summa += i
    return summa
