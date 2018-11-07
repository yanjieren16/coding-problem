"""
Given the root node of a binary search tree (BST) and a value.
You need to find the node in the BST that the node's value equals the given value. 
Return the subtree rooted with that node. 
If such node doesn't exist, you should return NULL.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def __init__(self):
        self.node = None

    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            print("Not found")
            self.node = None
            return None

        if root.val == val:
            print("Found")
            self.node = root

        if val < root.val:
            self.searchBST(root.left, val)

        elif val > root.val:
            self.searchBST(root.right, val)

        return self.node

    def print_tree(self, root, level=0):
        if root is None:
            return
        print("  " * level + str(root.val))
        self.print_tree(root.left, level+1)
        self.print_tree(root.right, level+1)
