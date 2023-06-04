#!/usr/bin/python3
"""Unittest class to test files"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):
    """Tescase to test max_integer function"""

    def test_empty(self):
        """Function to test for None input to max_integer"""
        self.assertIsNone(max_integer([]))

    def test_Max(self):
        """Function to test for Max number in a list"""
        self.assertEqual(max_integer([1, 2, 10, 3]), 10)

    def test_NotMax(self):
        """Function to test if not max number"""
        self.assertNotEqual(max_integer([1, 2, 10, 3]), 1)

    def test_TypeErr(self):
        """Function to test TypeErrors"""
        with self.assertRaises(TypeError):
            max_integer([1, "string", 2, 4,])

    def test_None(self):
        """Function to test None TypeErrors"""
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == "__main__":
    unittest.main()
