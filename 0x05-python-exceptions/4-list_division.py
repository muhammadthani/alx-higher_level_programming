#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    len(new_list) == list_length
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError):
            div = 0
            print(f"division by 0")
        except (TypeError):
            div = 0
            print(f"wrong type")
        except (IndexError):
            div = 0
            print(f"out of range")
        finally:
            new_list.append(div)
    return new_list
