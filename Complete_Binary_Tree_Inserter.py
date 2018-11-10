"""
A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

Write a data structure CBTInserter that is initialized with a complete binary tree and supports the following operations:

CBTInserter(TreeNode root) initializes the data structure on a given tree with head node root;
CBTInserter.insert(int v) will insert a TreeNode into the tree with value node.val = v so that the tree remains complete, and returns the value of the parent of the inserted TreeNode;
CBTInserter.get_root() will return the head node of the tree.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.queue = [root]

        while self.queue:
            curr = self.queue.pop()
            if curr.left:
                self.queue.insert(0, curr.left)
            if curr.right:
                self.queue.insert(0, curr.right)
            if curr.left is None or curr.right is None:
                self.queue.append(curr)
                break

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """

        while self.queue:
            curr = self.queue.pop()
            if curr.left is None:
                curr.left = TreeNode(v)
                self.queue.append(curr)
                self.queue.insert(0, curr.left)
                return curr.val

            if curr.right is None:
                curr.right = TreeNode(v)
                self.queue.insert(0, curr.right)
                return curr.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root
