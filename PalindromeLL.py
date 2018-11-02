"""
Palindrome linked list

1) Get the middle of the linked list.
2) Reverse the second half of the linked list.
3) Check if the first half and second half are identical.
4) Construct the original linked list by reversing the second half again and attaching it back to the first half

Time Complexity O(n)
Auxiliary Space: O(1)
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head is None or head.val is None:
            return True
        
        current = head
        length = 1
        while current.next:
            current = current.next
            length += 1

        if length % 2 == 0:
            start = length // 2 + 1
        else:
            start = (length + 1) // 2 + 1

        # set right pointer to head
        right = head
        right_pos = 1
        # move the pointer to the right part of the linked list
        while right_pos < start:
            right = right.next
            right_pos += 1

        right_part = self.reverse(right)

        left = head
        left_pos = 1
        right_pos = 1

        while left_pos < (length + 1) / 2:
            if left.val != right_part.val:
                return False
            else:
                left = left.next
                left_pos += 1
                right_part = right_part.next
                right_pos += 1

        return True

    def reverse(self, head):
        prev = None
        current = head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

    def print_node(self, head):
        current = head
        while current:
            print(current.val)
            current = current.next
