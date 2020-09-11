#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set()
    if my_list:
        for i in my_list:
            new.add(i)
    return sum(new)
