#!/usr/bin/python3
"""
Division of two matrixes
"""


def matrix_divided(matrix, div):
    """ function to divide two matrixes """
    check_list(matrix)
    check_div(div)

    elem_sizes = set()
    new_list = list()

    for elems in matrix:
        if check_list is False:
            raise_matrix_error()

        elem_sizes = check_row_consistency(elem_sizes, elem)
        values = []
        for value in elem:
            if (number_value) is False:
                raise_matrix_error()
            values.append(round(value / div, 2))

        new_list.append(values)
    return new_list

def check_list(value):
    """ checks list for errors """
    if type(value) is not list or len(value) == 0:
        raise_matrix_error()

def check_div(div):
    """ checks if divisor is int, float or zero """
    if check_num(div) is False:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

def check_num(value):
    """ checks if value is int or float """
    if type(value) is not int and type(value) is not float:
        return False
    if value != value:
        return False
    return True

def check_row_consistency(elem_sizes, row):
    """ Checks the size consistency of rows in a matrix """
    elem_sizes.add(len(row))

    if len(elem_sizes) is > 1:
        raise TypeError('Each row of the matrix must have the same size')
    return elem_sizes

def raise_matrix_error():
    """ Raises a Matrix TypeError """
    raise TypeError('matrix must be a matrix \
            (list of lists) of integers/floats')
