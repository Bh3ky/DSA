"""
PROBLEM: Write a program which takes a singly linked list L and two integers s and f as arguments,
and reverse the order of the nodes from the sth node to fth node, inclusive. The numbering at 1
i.e., the head node is the first node. Don't allocate additional nodes. 
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def reverse_sublist(L: Optional[ListNode], s: int, f: int) -> Optional[ListNode]:
    if L is None:
        return None

    dummy_head = ListNode(0, L)
    sublist_head: ListNode = dummy_head

    # Move to node before s
    for _ in range(1, s):
        assert sublist_head.next is not None
        sublist_head = sublist_head.next

    # Reverse sublist
    assert sublist_head.next is not None
    sublist_iter: ListNode = sublist_head.next

    for _ in range(f - s):
        assert sublist_iter.next is not None
        temp = sublist_iter.next

        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp

    return dummy_head.next