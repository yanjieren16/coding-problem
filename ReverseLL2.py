# Reverse a linked list from position m to n. Do it in one-pass
# 1 ≤ m ≤ n ≤ length of list
# Example:
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def reverseBetween(self, head, m, n):

        # if m == n, nothing needs to be reversed, just return the original linked list 
        if m == n:
            return head

        current = head
        pos = 1
        while pos < m:
            prev = current
            current = current.next
            pos += 1
        if m != 1:
            end = prev
        start = current

        prev = None
        while pos <= n:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            pos += 1
        if m != 1:
            end.next = prev
        else:
            head = prev
        start.next = current
        return head

    def print_node(self, head):
        current = head
        while current:
            print(current.val)
            current = current.next
