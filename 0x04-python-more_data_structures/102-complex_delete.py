#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keysto_del = []
    for i, j in a_dictionary.items():
        if j == value:
            keysto_del.append(i)
    for i in keysto_del:
        del a_dictionary[i]
    return a_dictionary
