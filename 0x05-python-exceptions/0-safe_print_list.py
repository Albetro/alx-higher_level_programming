#!/usr/bin/python3
def safe_print_list(my_list=[], j=0):
    try:
        for i in range(j):
            print(my_list[i], end="")
    except IndexError:
        j = i  # updates the value of x to index reached before exception occurred
    finally:
        print()
        return j
