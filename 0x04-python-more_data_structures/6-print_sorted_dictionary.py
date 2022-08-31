#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_dict = list(a_dictionary.keys())
    list_dict.sort()
    for i in list_dict:
        print("{}: {}".format(i, a_dictionary.get(i)))
