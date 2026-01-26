import unittest
from solution import Solution

class TestPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_basic_palindrome(self):
        self.assertTrue(
            self.solution.is_palindrome("A man, a plan, a canal, Panama.")
        )

    def test_another_palindrome(self):
        self.assertTrue(
            self.solution.is_palindrome("Able was I, ere I saw Elba!")
        )

    def test_not_palindrome(self):
        self.assertFalse(
            self.solution.is_palindrome("Ray a Ray")
        )

    def test_empty_string(self):
        self.assertTrue(
            self.solution.is_palindrome("")
        )

    def test_only_non_alphanumeric(self):
        self.assertTrue(
            self.solution.is_palindrome("!!!")
        )

if __name__ == "__main__":
    unittest.main()