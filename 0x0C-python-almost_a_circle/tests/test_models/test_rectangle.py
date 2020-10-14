#!/usr/bin/python3
"""Unittest for base.py
"""


import unittest
import pep8
import sys
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):

    def checking_docstring(self):
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIsNotNone(width.__doc__)
        self.assertIsNotNone(height.__doc__)
        self.assertIsNotNone(x.__doc__)
        self.assertIsNotNone(y.__doc__)
        self.assertIsNotNone(area.__doc__)
        self.assertIsNotNone(display.__doc__)
        self.assertIsNotNone(__str__.__doc__)
        self.assertIsNotNone(update.__doc__)
        self.assertIsNotNone(to_dictionary.__doc__)

    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects == 0
        cls.r1 = Rectangle(10, 2)
        cls.r3 = Rectangle(2, 4, 2, 2, 12)

if __name__ == '__main__':
    unittest.main()