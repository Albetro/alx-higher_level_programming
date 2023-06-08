#!/usr/bin/python3
import sys


if __name__ == "__main__":
    list_arg = sys.argv[1:]
    total = 0
    for m in list_arg:
        total = total + int(m)
    print(total)
