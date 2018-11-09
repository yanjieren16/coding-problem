"""
We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.
Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root is None:
            return None

        if self.is_remove(root.left):
            root.left = None
        if self.is_remove(root.right):
            root.right = None
        if root.left:
            self.pruneTree(root.left)
        if root.right:
            self.pruneTree(root.right)
        return root

    def is_remove(self, root):

        if root is None:
            return True
        elif root.val == 1:
            return False
        else:
            return self.is_remove(root.left) and self.is_remove(root.right)
