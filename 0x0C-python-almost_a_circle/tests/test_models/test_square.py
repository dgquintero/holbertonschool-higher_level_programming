#!/usr/bin/python3
"""
Tests for class square
"""


import unittest
import json
from models.base import Base
from models import square
Square = square.Square


class TestBaseDocuments(unittest.TestCase):
    """Tests to check base class documentation"""
    def test_class_docstring(self):
        """Tests to check class docstring"""
        self.assertTrue(len(Square.__doc__) >= 1)


class TestBaseFunc(unittest.TestCase):
    """Tests functionality of class"""
    def many_args(self):
        """test many args"""
        with self.assertRaises(TypeError):
            x = Square(2, 2, 2, 2, 2)

if __name__ == '__main__':
    unittest.main()
