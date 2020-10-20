#!/usr/bin/python3
common_elements = __import__('3-common_elements').common_elements

set_1 = [1, 2, 3, 4]
set_2 = [2, 8, 6, 4]
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
