# Unit tests for the pascal_triangle problem

import unittest
from pascal_triangle import Solution

class TestPascalTriangle(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_zero_rows(self):
        # Edge case: no rows requested
        self.assertEqual(self.solution.generate_pascal_triangle(0), [])

    def test_one_row(self):
        # Minimal valid input
        self.assertEqual(
            self.solution.generate_pascal_triangle(1),
            [[1]]
        )

    def test_two_rows(self):
        self.assertEqual(
            self.solution.generate_pascal_triangle(2),
            [[1], [1, 1]]
        )

    def test_four_rows(self):
        # Typical case
        self.assertEqual(
            self.solution.generate_pascal_triangle(4),
            [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1]
            ]
        )

    def test_five_rows(self):
        self.assertEqual(
            self.solution.generate_pascal_triangle(5),
            [
                [1],
                [1, 1],
                [1, 2, 1],
                [1, 3, 3, 1],
                [1, 4, 6, 4, 1]
            ]
        )

if __name__ == "__main__":
    unittest.main()