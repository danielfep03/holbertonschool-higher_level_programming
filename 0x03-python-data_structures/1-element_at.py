#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    count = len(my_list)
    if idx >= count:
        return None
    return my_list[idx]
