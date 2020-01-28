#!/usr/bin/python3
"""
Tests for class base
"""


import unittest
import json
from models import base
Base = base.Base


class TestBaseDocuments(unittest.TestCase):
    """Tests to check base class documentation"""
    def test_class_docstring(self):
        """Tests to check class docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)


class TestBaseFunc(unittest.TestCase):
    """Tests functionality of class"""
    def many_args(self):
        """test many args"""
        with self.assertRaises(TypeError):
            b = Base(2, 2)

if __name__ == '__main__':
    unittest.main()
