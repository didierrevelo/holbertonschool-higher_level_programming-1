#!/usr/bin/python3
"""Unittest for base.py
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def tests_id(self):
        b = Base()
        self.assertEqual(1, b.id)

if __name__ == '__main__':
    unittest.main()
