#!/usr/bin/python3
''' File to learn to use inheritance '''


class MyList(list):
    '''Class that inherits from list'''

    def print_sorted(self):
        new_list = self.copy()
        new_list.sort()
        print(new_list)
