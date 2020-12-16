#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        tuple_sentence = (0, None)
    else:
        tuple_sentence = (len(sentence), sentence[0])
    return tuple_sentence
