#!/usr/bin/python3
''' Change compartions value '''


class MyInt(int):
    ''' Class to change comparations values'''
    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
