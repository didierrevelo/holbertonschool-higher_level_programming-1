#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = ""
    a = 0
    for i in str:
        if a != n:
            str2 = str2 + i
        a = a + 1
    return str2
