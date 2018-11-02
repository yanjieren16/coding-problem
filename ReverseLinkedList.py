# Reverse Linked List

Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# iterative
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        previous = None
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        head = previous
        return head

    def print_node(self, head):
        current = head
        while current:
            print(current.val)
            current = current.next
            
# recursive
class Solution2:

    def __init__(self):
        self.head = None

    def reverseList(self, first, prev):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if first.next is None:
            self.head = first

            first.next = prev
            return

        rest = first.next

        first.next = prev

        self.reverseList(rest, first)

    def reverse(self):
        if self.head is None:
            return
        self.reverseList(self.head, None)

    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_node(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next

