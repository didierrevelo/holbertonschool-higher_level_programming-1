#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list[:]
    if my_list:
        for i, x in enumerate(new):
            if x == search:
                new[i] = replace
        return new
