#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for  x in range(len(matrix)):
        for i  in range(len(matrix[x])):
            if  i != 0:
                print(" ", end=" ")       
            print("{:d}".format(matrix[x][i]), end="")
        print("")
