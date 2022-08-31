#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cp_list = list(map(lambda x: replace if x == search else x, my_list))
    return (cp_list)
