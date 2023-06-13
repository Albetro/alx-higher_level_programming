#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    m = list(tuple_a)  # conveet tuples to list for modification
    n = list(tuple_b)

    while len(m) < 2:
        m.append(0)
    while len(n) < 2:
        n.append(0)

    m = m[:2]  # only two elements per tuple to be used
    n = n[:2]
    return (m[0] + n[0], m[1] + n[1])
