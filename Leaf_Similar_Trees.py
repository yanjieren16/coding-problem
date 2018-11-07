“”“
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
”“”

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def leafSimilar(self, root1, root2):

        list1 = []
        list2 = []
        self.traverse(root1, list1)
        self.traverse(root2, list2)

        if len(list1) != len(list2):
            return False
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False
        return True

    def traverse(self, root, list):
        if root is None:
            return
        self.traverse(root.left, list)
        self.traverse(root.right, list)
        if root.left is None and root.right is None:
            list.append(root.val)


    def print_tree(self, root, level=0):
        if root is None:
            return
        print("  " * level + str(root.val))
        self.print_tree(root.left, level+1)
        self.print_tree(root.right, level+1)
