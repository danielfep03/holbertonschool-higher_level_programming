#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        new_list = []
        count = len(my_list)
        for i in range(0, count):
            new_list.append(my_list[i])
        if idx < 0 or idx >= count:
            return new_list
        new_list[idx] = element
        return new_list
