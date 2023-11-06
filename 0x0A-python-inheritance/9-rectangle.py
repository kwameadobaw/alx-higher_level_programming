#!/usr/bin/python3
"""A rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.__width = width
        self.__height = height

        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return ("[Rectangle {}/{}]".format(self.__width, self.__height))
