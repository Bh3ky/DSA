"""
PROBLEM: Write a program that takes the head of a singly linked list and returns null
if there doesn't exist a cycle in the list, and the node at the start of the cycle if
there is a cycle in the list. (You don't know the length of the list in advance).

HINT: Consider using two iterators, one fast and one slow.
"""

# solution.py

from typing import Optional


class ListNode:
    def __init__(self, value: int = 0, next: Optional["ListNode"] = None):
        self.value: int = value
        self.next: Optional["ListNode"] = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        slow: Optional[ListNode] = head
        fast: Optional[ListNode] = head

        # Step 1: Detect if cycle exists
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            # No cycle
            return None

        # Step 2: Find start of cycle
        pointer_from_head: Optional[ListNode] = head
        pointer_from_meeting: Optional[ListNode] = slow

        while pointer_from_head != pointer_from_meeting:
            pointer_from_head = pointer_from_head.next
            pointer_from_meeting = pointer_from_meeting.next

        return pointer_from_head
    

# Time complexity: O(n)
# Space complexity: O(1)