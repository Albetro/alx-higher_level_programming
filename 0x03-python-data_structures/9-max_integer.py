#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    Int_Max = my_list[0]
    for i in my_list:
        if i > Int_Max:
            Int_Max = i
    return Int_Max
