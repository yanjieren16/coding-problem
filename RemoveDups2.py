# Given a sorted linked list,
# delete all nodes that have duplicate numbers, 
# leaving only distinct numbers from the original list.

# example: 
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5

# example:
# Input: 1->1->1->2->3
# Output: 2->3

Definition for singly-linked list.
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
        
class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        elif head.next is None:
            return head

        current = head

        dict = {}
        while current:
            if current.val in dict:
                dict[current.val] += 1
            else:
                dict[current.val] = 0
            current = current.next

        while dict[head.val]:
            head = head.next
            if head is None:
                return []

        current = head
        next_node = head.next

        while next_node:
            if dict[next_node.val] == 0:
                current.next = next_node
                current = current.next
                next_node = next_node.next
            else:
                next_node = next_node.next
            if next_node is None and current.next:
                if dict[current.next.val] > 0:
                    current.next = None

        return head
