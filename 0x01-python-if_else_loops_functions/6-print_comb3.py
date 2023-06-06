#!/usr/bin/python3
for j in range(0, 10):
    for k in range(j+1, 10):
        print("{:d}".format(j), end='')
        if j == 8 and k == 9:
            print("{:d}".format(k), end='\n')
        else:
            print("{:d}".format(k), end=', ')
