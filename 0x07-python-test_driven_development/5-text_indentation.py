#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    skip_next = False
    for idx, i in enumerate(text):
        if skip_next:
            skip_next = False
            continue
        if i in [".", "?", ":"]:
            print(i, end="\n")
            print()
            skip_next = True
        else:
            print(i, end="")
