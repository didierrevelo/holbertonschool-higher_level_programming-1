#!/usr/bin/python3
import sys

def pascal_triangle(n):
    """Funcion que recibe como parametro el número de filas del triángulo"""
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        new_row = [1]
        result = pascal_triangle(n-1)
        last_row = result[-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        result.append(new_row)
    return result