import unittest
from solution import Solution

class TestReplaceAndRemove(unittest.TestCase):
    def test_basic_case(self):
        s = ['a', 'c', 'd', 'b', 'b', 'c', 'a', None, None]
        size = 7
        final_size = Solution().replace_and_remove(s, size)
        self.assertEqual(s[:final_size], ['d', 'd', 'c', 'd', 'c', 'd', 'd'])

    def test_no_bs(self):
        s = ['a', 'a', 'c', None, None]
        size = 3
        final_size = Solution().replace_and_remove(s, size)
        self.assertEqual(s[:final_size], ['d', 'd', 'd', 'd', 'c'])

    def test_no_as(self):
        s = ['c', 'b', 'd']
        size = 3
        final_size = Solution().replace_and_remove(s, size)
        self.assertEqual(s[:final_size], ['c', 'd'])

    def test_all_bs(self):
        s = ['b', 'b', 'b']
        size = 3
        final_size = Solution().replace_and_remove(s, size)
        self.assertEqual(final_size, 0)

    def test_empty(self):
        s = []
        size = 0
        final_size = Solution().replace_and_remove(s, size)
        self.assertEqual(final_size, 0)

if __name__ == "__main__":
    unittest.main()