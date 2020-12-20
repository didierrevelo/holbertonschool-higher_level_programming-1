#!/usr/bin/python3
"""
6-peak.py
"""


def find_peak(list_of_integers):
    """
    finds a peak in a list of unsorted integers.
    """
    l1 = 0
    l2 = len(list_of_integers) - 1
    li = list_of_integers
    if li is None:
        return None
    if len(li) == 1:
        return li[0]
    
    while  l1 < l2:
        mid = (l2 + l1) // 2
        if li[mid] > li[mid + 1] and li[mid] > li[mid + 1]:
            return li[mid]
        if li[mid] < li[mid + 1] and li[mid] > li[mid - 1]:
            return li[mid + 1]
        return max(li)