#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for key_iterator, value_iterator in a_dictionary.items():
        if key_iterator == key:
            if value == value_iterator:
                return a_dictionary
            else:
                a_dictionary[key] = value

    a_dictionary[key] = value
    return a_dictionary
