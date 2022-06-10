#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    another_dictionary = a_dictionary.copy()

    for k, v in another_dictionary.items():
        another_dictionary[k] = v * 2
    
    return another_dictionary
