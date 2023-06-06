#!/usr/bin/python3
def remove_char_at(str, n):
    a_new_string = ""
    for q in range(len(str)):
        if q != n:
            a_new_string = a_new_string + str[q]
    return a_new_string
