import unittest
from solution import Solution

class TestBaseConversion(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        self.assertEqual(self.solution.convert_base("615", 7, 13), "1A7")

    def test_decimal_to_hex(self):
        self.assertEqual(self.solution.convert_base("255", 10, 16), "FF")

    def test_hex_to_decimal(self):
        self.assertEqual(self.solution.convert_base("A", 16, 10), "10")

    def test_negative_number(self):
        self.assertEqual(self.solution.convert_base("-1A", 16, 10), "-26")

    def test_zero(self):
        self.assertEqual(self.solution.convert_base("0", 10, 2), "0")

if __name__ == "__main__":
    unittest.main()