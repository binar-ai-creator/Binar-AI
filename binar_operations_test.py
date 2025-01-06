# binar_operations_test.py

import unittest
from binar_operations import bin_add, bin_subtract, bin_multiply, bin_divide, bin_modulo

class TestBinarOperations(unittest.TestCase):

    def test_bin_add(self):
        self.assertEqual(bin_add("101", "110"), "1011")
        
    def test_bin_subtract(self):
        self.assertEqual(bin_subtract("1101", "101"), "1000")

    def test_bin_multiply(self):
        self.assertEqual(bin_multiply("101", "11"), "1111")

    def test_bin_divide(self):
        self.assertEqual(bin_divide("1101", "11"), "11")
        self.assertEqual(bin_divide("1101", "0"), "Error: Division by zero")

    def test_bin_modulo(self):
        self.assertEqual(bin_modulo("1101", "11"), "1")

if __name__ == "__main__":
    unittest.main()
