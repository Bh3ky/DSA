# test.py
import unittest
from solution import int_to_string, string_to_int


class TestStringIntegerConversion(unittest.TestCase):

    # -------- Tests for int_to_string --------

    def test_int_to_string_positive(self):
        self.assertEqual(int_to_string(314), "314")

    def test_int_to_string_single_digit(self):
        self.assertEqual(int_to_string(7), "7")

    def test_int_to_string_zero(self):
        self.assertEqual(int_to_string(0), "0")

    def test_int_to_string_negative(self):
        self.assertEqual(int_to_string(-42), "-42")

    def test_int_to_string_large_number(self):
        self.assertEqual(int_to_string(123456), "123456")

    # -------- Tests for string_to_int --------

    def test_string_to_int_positive(self):
        self.assertEqual(string_to_int("314"), 314)

    def test_string_to_int_single_digit(self):
        self.assertEqual(string_to_int("7"), 7)

    def test_string_to_int_zero(self):
        self.assertEqual(string_to_int("0"), 0)

    def test_string_to_int_negative(self):
        self.assertEqual(string_to_int("-42"), -42)

    def test_string_to_int_large_number(self):
        self.assertEqual(string_to_int("123456"), 123456)


if __name__ == "__main__":
    unittest.main()