#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    pos = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        pos[idx] = element
        return pos
    