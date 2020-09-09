#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j, h in enumerate(i):
            print("{:d}".format(h), end="")
            if (j < len(i) - 1):
                print("{}".format(" "), end="")
        print()
