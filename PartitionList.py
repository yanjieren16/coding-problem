        
"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Example:
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

Initialize first and last nodes of below three linked lists as NULL.
Linked list of values smaller than x.
Linked list of values equal to x.
Linked list of values greater than x.
Iterate through the original linked list.
If a node’s value is less than x then append it at the end of smaller list.
If the value is equal to x, then at the end of equal list.
And if value is greater, then at the end of greater list.
Concatenate three lists
Needs extra space
"""




# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None




class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None or head.val is None:
            return head

        small_list = ListNode(None)
        small_head = small_list
        large_list = ListNode(None)
        large_head = large_list

        curr = head
        while curr:
            if curr.val < x:
                new_node = ListNode(curr.val)
                small_list.next = new_node
                small_list = small_list.next
            elif curr.val >= x:
                new_node = ListNode(curr.val)
                large_list.next = new_node
                large_list = large_list.next
            curr = curr.next

        small_list.next = large_head.next
        return small_head.next

    def find_first(self, head):
        curr = head
        while curr:
            if curr.val < x:
                return curr
            else:
                curr = curr.next

    def print_node(self, head):
        current = head
        while current:
            print(current.val)
            current = current.next
