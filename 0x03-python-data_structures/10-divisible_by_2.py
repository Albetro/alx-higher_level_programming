#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_l = []
    for l in my_list:
        if l % 2 == 0:
            new_l.append(True)
        else:
            new_l.append(False)
    return new_l
