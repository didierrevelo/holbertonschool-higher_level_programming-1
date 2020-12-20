#!/usr/bin/python3
"""
6-peak.py
"""


def find_peak(list_of_integers):
    if not list_of_integers:
        return
    init = 0
    finish = len(list_of_integers) - 1
    return findPeak_e(list_of_integers, init, finish)


def findPeak_e(A, init, finish):
    """
    finds a peak in a list of unsorted integers.
    """
    if init == finish:
        return A[finish]
    mid = (init + finish)//2
    if A[mid] > A[mid + 1]:
        return findPeak_e(A, init, mid)
    return findPeak_e(A, mid + 1, finish)
