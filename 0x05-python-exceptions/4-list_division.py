#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_result = []
    for idx in range(list_length):
        try:
            div = my_list_1[idx] / my_list_2[idx]
        except(TypeError, ZeroDivisionError, IndexError) as Error:
            if (isinstance(Error, ZeroDivisionError)):
                print("division by 0")
            elif (isinstance(Error, TypeError)):
                print("wrong type")
            elif (isinstance(Error, IndexError)):
                print("out of range")
            list_result.append(0)
        finally:
            list_result.append(div)
    return list_result
