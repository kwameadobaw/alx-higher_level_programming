#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_char = sentence[0]
    if length < 0:
        first_char = None
    output = length, first_char
    return output
