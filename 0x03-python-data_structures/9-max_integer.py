#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == ():
        return None
    else:
        this_num = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > this_num:
                this_num = my_list[i]
        return (this_num)
