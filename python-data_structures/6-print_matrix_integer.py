#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        #{:^3} format specifier puts elements in width of 3
        #*row unpacks row elements into format
        print("| {:^3} {:^3} {:^3} |".format(*row))
