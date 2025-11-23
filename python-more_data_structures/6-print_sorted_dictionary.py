#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = dict(sorted(a_dictionary.items()))
    for i in sorted_dict.items():
        print(str(i.key) + ": " + str(i.value()))
