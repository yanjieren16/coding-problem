"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        # compare where one has smaller start. always return the smaller head
        if l1.val <= l2.val:
            first = l1
            sec = l2
        else:
            first = l2
            sec = l1

        curr1 = first
        curr2 = sec

        prev1 = None
        prev2 = None

        while True:
            while curr1.val <= curr2.val:
                prev1 = curr1
                curr1 = curr1.next
                if curr1 is None:
                    prev1.next = curr2
                    return first
            prev1.next = curr2

            while curr1.val > curr2.val:
                prev2 = curr2
                curr2 = curr2.next
                if curr2 is None:
                    prev2.next = curr1
                    return first
            prev2.next = curr1

    def print_node(self, head):
        current = head
        while current:
            print(current.val)
            current = current.next
