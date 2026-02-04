""" 
PROBLEM: Wrtie a program that takes two lists, assumed to be be sorted,
and return their merge. Note: the only field your program can change in
a node is its next field. 
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge_two_sorted_lists(self, L1, L2):
        # dummy node to simplify edge cases
        dummy = ListNode()
        tail = dummy

        # traverse both lists while neither of them is equal to being empty/zero
        while L1 and L2:
            if L1.val <= L2.val:
                # attach L1 node
                tail.next = L1 
                L1 = L1.next # move L1 forward

            else:
                # attach L2 node
                tail.next = L2 
                L2 = L2.next  # move L2 forward

            # we move the tail forward
            tail = tail.next

        # attach remaining nodes 
        tail.next = L1 if L1 else L2

        # return the merged list. note we skip dummy here
        return dummy.next