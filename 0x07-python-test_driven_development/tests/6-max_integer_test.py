#!/usr/bin/python3
"""UNittest for the function max_integer"""


import unittest
max_integer = __import__("6-max_integer").max_integer


class MyTestCase(unittest.TestCase):
    """Unittest class with some test casses for the function max_integer"""
    def testmaxinteger(self):
        self.assertEqual(max_integer([1, 28, 3]), 28)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer("abcdefghijklmnopqrstuvwxyz"), 'z')
        self.assertIsNone(max_integer())
if __name__ == "__main__":
    unittest.main()
