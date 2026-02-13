# test.py

import unittest
from solution import Solution, ListNode


class TestSolution(unittest.TestCase):

    def create_cycle_list(self):
        # Create nodes
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)
        node5 = ListNode(5)

        # Connect nodes
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5

        # Create cycle (node5 -> node3)
        node5.next = node3

        return node1, node3  # head and expected cycle start

    def test_cycle_exists(self):
        head, expected_start = self.create_cycle_list()
        result = Solution().detectCycle(head)
        self.assertEqual(result, expected_start)

    def test_no_cycle(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node1.next = node2

        result = Solution().detectCycle(node1)
        self.assertIsNone(result)

    def test_empty_list(self):
        result = Solution().detectCycle(None)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()