#!/usr/bin/python3
"""Defines unittest for base.py"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Class to test the base Class"""

    def test_No_Args(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)

    def test_With_Three_Args(self):
        base = Base()
        base1 = Base()
        base2 = Base()
        self.assertEqual(base.id, base2.id - 2)

    def test_With_None(self):
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def test_With_Args(self):
        base1 = Base(40)
        self.assertEqual(40, base1.id)

    def test_Id_after_uniq_declarations(self):
        base1 = Base()
        base2 = Base(30)
        base3 = Base()
        self.assertEqual(base1.id, base3.id - 1)

    def test_str_id(self):
        base1 = Base("Daniel")
        self.assertEqual("Daniel", base1.id)

    def test_Id_Public(self):
        base1 = Base(50)
        base1.id = 5
        self.assertEqual(5, base1.id)

    def test_Float_Id(self):
        base1 = Base(10.1)
        self.assertEqual(10.1, base1.id)

    def test_Id_Complex(self):
        base1 = Base(complex(10))
        self.assertEqual(complex(10), base1.id)

    def test_Dictionary_Id(self):
        base1 = Base({"name": "Daniel"})
        self.assertEqual({"name": "Daniel"}, base1.id)

    def test_Tuples(self):
        base1 = Base((1, 2, 3))
        self.assertEqual((1, 2, 3), base1.id)

    def test_Bools(self):
        base1 = Base(True)
        self.assertEqual(True, base1.id)

    def test_List(self):
        base1 = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], base1.id)

    def test_bytes(self):
        base1 = Base(b'Hello')
        self.assertEqual(b'Hello', base1.id)

    def test_bytearray(self):
        base1 = Base(bytearray(b'abeg'))
        self.assertEqual(bytearray(b'abeg'), base1.id)

    def test_Memoryview(self):
        base1 = Base(memoryview(b'hello'))
        self.assertEqual(memoryview(b'hello'), base1.id)

    def test_str_float(self):
        base1 = Base(float('inf'))
        self.assertEqual(float('inf'), base1.id)

    def test_nan(self):
        base1 = Base(float('nan'))
        self.assertNotEqual(float('nan'), base1.id)

    def test_2Args(self):
        with self.assertRaises(TypeError):
            Base(4, "hello")


if __name__ == "__main__":
    unittest.main()
