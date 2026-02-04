import unittest
from solution import Solution, ListNode


def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class TestMergeSortedLists(unittest.TestCase):

    def test_basic_case(self):
        L1 = build_linked_list([1, 3, 5])
        L2 = build_linked_list([2, 4, 6])
        result = Solution().merge_two_sorted_lists(L1, L2)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3, 4, 5, 6])

    def test_one_empty(self):
        L1 = build_linked_list([])
        L2 = build_linked_list([1, 2, 3])
        result = Solution().merge_two_sorted_lists(L1, L2)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3])

    def test_both_empty(self):
        result = Solution().merge_two_sorted_lists(None, None)
        self.assertEqual(linked_list_to_list(result), [])

    def test_duplicate_values(self):
        L1 = build_linked_list([1, 2, 2])
        L2 = build_linked_list([1, 2, 3])
        result = Solution().merge_two_sorted_lists(L1, L2)
        self.assertEqual(linked_list_to_list(result), [1, 1, 2, 2, 2, 3])


if __name__ == "__main__":
    unittest.main()