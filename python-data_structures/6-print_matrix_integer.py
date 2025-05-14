#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        #{:3} formats each number to be right-aligned within 3 spaces
        print("{:3} {:3} {:3} |".format(row[0], row[1], row[2]))
