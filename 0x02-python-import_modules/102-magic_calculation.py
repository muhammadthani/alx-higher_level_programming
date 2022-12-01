#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        l = add(a, b)
        for i in range(4, 6):
            l = add(l, i)
        return (l)
    else:
        return (sub(a, b))
