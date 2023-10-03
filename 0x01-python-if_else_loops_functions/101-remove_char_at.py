#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    result_str = ""

    for i in range(len(str)):
        if i != n:
            result_str += str[i]

    return result_str
