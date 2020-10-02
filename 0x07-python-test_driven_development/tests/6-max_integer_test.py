#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def testForImport(self):
        self.assertTrue(__import__('6-max_integer').max_integer)

    def test(self):
        self.assertEqual(max_integer([1, 3, 2, 4]), 4)
        self.assertEqual(max_integer([1, 2, 4, 52]), 52)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(['what', 'off', 'gumby']), 'what')
        self.assertRaises(TypeError, max_integer, [1, 4, 'A'])
        self.assertRaises(KeyError, max_integer, {'a': 2, 'b': 1, 'c': 3})

    def test_max_integer(self):
        """ a method with different cases """
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([4, 6, 2, 10, 1]), 10)

if __name__ == '__main__':
    unittest.main()
