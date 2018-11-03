"""
Write a program to find the node at which the intersection of two singly linked lists begins.
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
may assume there are no cycles anywhere in the entire linked structure.
code should preferably run in O(n) time and use only O(1) memory.

Thoughts:
Using difference of node counts
Get count of the nodes in the first list, let count be c1.
Get count of the nodes in the second list, let count be c2.
Get the difference of counts d = abs(c1 – c2)
Traverse the bigger list from the first node till d nodes so that from here onwards both the lists have equal no of nodes.
Traverse both the lists in parallel till we come across a common node.
(Note that getting a common node is done by comparing the address of the nodes)
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headA.val is None:
            return None

        if headB is None or headB.val is None:
            return None

        len_a = self.length(headA)
        len_b = self.length(headB)

        if len_a >= len_b:
            diff = len_a - len_b
            return self.find_node(headA, headB, diff)
        else:
            diff = len_b - len_a
            return self.find_node(headB, headA, diff)

    def find_node(self, long_list, short_list, difference):
        p_long = long_list
        while difference > 0:
            p_long = p_long.next
            difference -= 1

        p_short = short_list
        while p_long:
            if p_long != p_short:
                p_long = p_long.next
                p_short = p_short.next
            else:
                return p_long
        return None

    def length(self, head):
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        return length

    def print_node(self, head):
        current = head
        while current:
            print(current.val)
            current = current.next
