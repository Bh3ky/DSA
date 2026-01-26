import unittest
from solution import Solution

class TestReverseWords(unittest.TestCase):
    def test_basic_case(self):
        s = bytearray(b"Alice likes Bob")
        Solution().reverse_words(s)
        self.assertEqual(s.decode(), "Bob likes Alice")

    def test_single_word(self):
        s = bytearray(b"Hello")
        Solution().reverse_words(s)
        self.assertEqual(s.decode(), "Hello")

    def test_multiple_spaces(self):
        s = bytearray(b"ram is costly")
        Solution().reverse_words(s)
        self.assertEqual(s.decode(), "costly is ram")

    def test_empty_string(self):
        s = bytearray(b"")
        Solution().reverse_words(s)
        self.assertEqual(s.decode(), "")

if __name__ == "__main__":
    unittest.main()