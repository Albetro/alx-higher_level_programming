#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    real_elements = 0
    for w in range(x):
        try:
            print("{:d}".format(my_list[w]), end="")
            real_elements += 1
        except(ValueError, TypeError):
            pass
    print()
    return real_elements
