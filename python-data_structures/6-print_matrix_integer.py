#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        non_row = row + [''] * (3 - len(row))
        print("{:d} {:d} {:d}".format(non_row[0], non_row[1], non_row[2]))
    if not matrix:
        print()
