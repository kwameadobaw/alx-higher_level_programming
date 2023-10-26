#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def testorderedlist(self):
        ordered_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(ordered_list), 5)

    def testunorderedlist(self):
        unordered_list = [1, 2, 5, 3, 4]
        self.assertEqual(max_integer(unordered_list), 5)

    def testnegatives(self):
        negatives = [-1, -1, -3, -4, -5]
        self.assertEqual(max_integer(negatives), -1)
        self.assertEqual(max_integer([1, 2, 3 , -4]), 3)
        
    def testfloat(self):
        self.assertEqual(max_integer([23.1, 16.3, 16.2, 23.95, 16.23]), 23.95)

    def testempty(self):
        self.assertEqual(max_integer([]), None)

    def testonenumber(self):
        self.assertEqual(max_integer([6]), 6)

    def testintandfloat(self):
        self.assertEqual(max_integer([5, 3.5, 6, -9, 10]), 10)

    def teststring(self):
        strings = ["Kwame", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def teststring(self):
        string = "Kwame"
        self.assertEqual(max_integer(string), 'w')

    def testemptystring(self):
        self.assertEqual(max_integer(""), None)



if __name__ == '__main__':
    unittest.main()
