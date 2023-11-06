#!/usr/bin/python3
class MyInt(int):
    def __eq__(self, value):
        return int(self) != int(value)

    def __ne__(self, value):
        return int(self) == int(value)
