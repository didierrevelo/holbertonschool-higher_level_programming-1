#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        mayor = my_list[0]
        for j in my_list:
            if j > mayor:
                mayor = j
        return (mayor)
