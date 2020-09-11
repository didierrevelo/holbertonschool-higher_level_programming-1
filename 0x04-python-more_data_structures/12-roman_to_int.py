#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or len(roman_string) == 0:
        return 0
    r_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(0, len(roman_string)):
        if i == 0 or r_num[roman_string[i]] <= r_num[roman_string[i - 1]]:
            result += r_num[roman_string[i]]
        else:
            result += r_num[roman_string[i]] - 2 * r_num[roman_string[i - 1]]
    return result
