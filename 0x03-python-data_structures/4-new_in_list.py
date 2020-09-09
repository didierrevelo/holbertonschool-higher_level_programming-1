#!/usr/bin/python3
if __name__ == "__main__":
    new_in_list(0, 0, 0)


def new_in_list(my_list, idx, element):
    if idx > 0 or idx < len(my_list) - 1:
        my_list = my_list.copy()
        my_list[idx] = element
    return (my_list)
