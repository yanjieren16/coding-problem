"""
Remove all elements from a linked list of integers that have value val.
Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None or head.val is None:
            return head
        
        while head.val == val:
            head = head.next
            if head is None:
                return head
            
        current = head
        
        prev = None
        while current:
            while current.val != val:
                prev = current
                current = current.next
                if current is None:
                    prev.next = None
                    return head
            while current.val == val:
                current = current.next
                if current is None:
                    prev.next = None
                    return head
            prev.next = current
        return head
