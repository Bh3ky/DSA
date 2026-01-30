import unittest
from solution import Solution


class TestLookAndSay(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_base_case(self):
        # n = 1 should return the starting value
        self.assertEqual(self.solution.look_and_say(1), "1")

    def test_small_values(self):
        self.assertEqual(self.solution.look_and_say(2), "11")
        self.assertEqual(self.solution.look_and_say(3), "21")
        self.assertEqual(self.solution.look_and_say(4), "1211")

    def test_medium_values(self):
        self.assertEqual(self.solution.look_and_say(5), "111221")
        self.assertEqual(self.solution.look_and_say(6), "312211")

    def test_larger_value(self):
        self.assertEqual(self.solution.look_and_say(7), "13112221")

    def test_return_type(self):
        # Ensure the return type is string
        result = self.solution.look_and_say(5)
        self.assertIsInstance(result, str)


if __name__ == "__main__":
    unittest.main()