#!/usr/bin/python3
def max_integer(my_list=[]):
    for i in enumerate(my_list):
        if i == 0:
            return (None)
    mayor = my_list[0]
    for j in my_list:
        if j > mayor:
            mayor = j
    return (mayor)
