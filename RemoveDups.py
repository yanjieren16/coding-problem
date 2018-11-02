# remove node from sorted Singly linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        current = head
        next_node = current.next
        while next_node:
            while current.val == next_node.val:
                current.next = next_node.next
                next_node = next_node.next
                if next_node is None:
                    current.next = None
                    return head
            current = next_node
            next_node = next_node.next
        return head

    def print_node(self, head):
        current = head
        while current:
            print(current.val)
            current = current.next
