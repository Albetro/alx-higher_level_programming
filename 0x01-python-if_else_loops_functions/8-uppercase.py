#!/usr/bin/python3
def uppercase(str):
    str_upper = ""
    for q in str:
        if ord(q) >= 97 and ord(q) <= 122:
            str_upper = str_upper + chr(ord(q) - 32)
        else:
            str_upper = str_upper + q
    print("{}".format(str_upper))
