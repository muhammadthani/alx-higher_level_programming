#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for a in new_list:
        if a % 2 == 0:
            new_list[a] = True
        elif a % 2 != 0:
            new_list[a] = False
    return (new_list)
