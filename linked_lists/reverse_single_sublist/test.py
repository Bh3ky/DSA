import unittest
from solution import ListNode, reverse_sublist


def build_linked_list(values):
    """Helper: build linked list from Python list"""
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def linked_list_to_list(head):
    """Helper: convert linked list back to Python list"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class TestReverseSublist(unittest.TestCase):

    def test_middle_sublist(self):
        L = build_linked_list([1, 2, 3, 4, 5])
        result = reverse_sublist(L, 2, 4)
        self.assertEqual(linked_list_to_list(result), [1, 4, 3, 2, 5])

    def test_start_at_head(self):
        L = build_linked_list([1, 2, 3, 4, 5])
        result = reverse_sublist(L, 1, 3)
        self.assertEqual(linked_list_to_list(result), [3, 2, 1, 4, 5])

    def test_end_at_tail(self):
        L = build_linked_list([1, 2, 3, 4, 5])
        result = reverse_sublist(L, 3, 5)
        self.assertEqual(linked_list_to_list(result), [1, 2, 5, 4, 3])

    def test_single_element_sublist(self):
        L = build_linked_list([1, 2, 3])
        result = reverse_sublist(L, 2, 2)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3])

    def test_full_list_reverse(self):
        L = build_linked_list([1, 2, 3, 4])
        result = reverse_sublist(L, 1, 4)
        self.assertEqual(linked_list_to_list(result), [4, 3, 2, 1])

    def test_single_node_list(self):
        L = build_linked_list([1])
        result = reverse_sublist(L, 1, 1)
        self.assertEqual(linked_list_to_list(result), [1])


if __name__ == "__main__":
    unittest.main()