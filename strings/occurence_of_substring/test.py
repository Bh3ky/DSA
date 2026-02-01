import unittest
from solution import Solution

class TestRabinKarp(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(Solution().strStr("GACGCCA", "CGC"), 2)

    def test_no_match(self):
        self.assertEqual(Solution().strStr("AAAAA", "B"), -1)

    def test_exact_match(self):
        self.assertEqual(Solution().strStr("hello", "hello"), 0)

    def test_empty_pattern(self):
        self.assertEqual(Solution().strStr("abc", ""), 0)

    def test_pattern_longer(self):
        self.assertEqual(Solution().strStr("abc", "abcd"), -1)

if __name__ == "__main__":
    unittest.main()