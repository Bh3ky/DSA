import unittest
from solution import Solution 

class TestRLE(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_encode_basic(self):
        self.assertEqual(
            self.sol.encode("aaaabcccaa"),
            "4a1b3c2a"
        )

    def test_encode_single_char(self):
        self.assertEqual(
            self.sol.encode("a"),
            "1a"
        )

    def test_decode_basic(self):
        self.assertEqual(
            self.sol.decode("3e4f2e"),
            "eeeffffee"
        )

    def test_decode_multi_digit(self):
        self.assertEqual(
            self.sol.decode("12a"),
            "aaaaaaaaaaaa"
        )

    def test_round_trip(self):
        original = "aaabbccccdd"
        encoded = self.sol.encode(original)
        decoded = self.sol.decode(encoded)
        self.assertEqual(decoded, original)

if __name__ == "__main__":
    unittest.main()