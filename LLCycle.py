"""
Given a linked list, determine if it has a cycle in it.

Thoughts:
Move one pointer by one and other pointer by two.
If these pointers meet at same node then there is a loop.
If pointers do not meet then linked list doesn’t have loop.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        elif head.next is None:
            return False
        elif head.next.next is None:
            return False

        fast = head
        slow = head
        while fast.next:
            fast = fast.next.next
            if fast is None:
                return False
            slow = slow.next
            if fast == slow:
                return True
        return False

    def print_node(self, head):
        current = head
        while current:
            print(current.val)
            current = current.next
