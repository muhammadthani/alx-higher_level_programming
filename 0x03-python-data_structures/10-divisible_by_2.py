#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    len(new_list) == len(my_list)
    for a in new_list:
        if a % 2 == 0:
            new_list[a] = True
        else:
            new_list[a] = False
    return (new_list)
