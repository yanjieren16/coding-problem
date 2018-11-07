# Given two binary trees, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    
    def isSameTree(self, p, q):

        if p is None and q is None:
            return True
        if p is None and q:
            return False
        if q is None and p:
            return False

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def print_tree(self, root, level=0):
        if root is None:
            return
        print("  " * level + str(root.val))
        self.print_tree(root.left, level+1)
        self.print_tree(root.right, level+1)
