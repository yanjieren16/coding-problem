'''

# Recursive method
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def invertTree(self, root):

        #  The inverse of a tree with root r,
        #  and subtrees right and left, is a tree with root r,
        #  whose right subtree is the inverse of left,
        #  and whose left subtree is the inverse of right.

        if root is not None:
            left = self.invertTree(root.left)
            right = self.invertTree(root.right)
            root.left = right
            root.right = left
        return root

    def print_tree(self, root, level=0):
        if root is None:
            return
        print("  " * level + str(root.val))
        self.print_tree(root.left, level+1)
        self.print_tree(root.right, level+1)
'''

# Iterative method
'''
Goal is to swap the left and right child of all nodes in the tree.
Use a queue to store nodes whose left and right child have not been swapped yet.
Initially, only the root is in the queue.
As long as the queue is not empty, remove the next node from the queue, swap its children, 
and add the children to the queue.
Null nodes are not added to the queue. 
The queue will be empty and all the children swapped, return the original root.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def invertTree(self, root):

        queue = []
        queue.insert(0, root)
        while queue:
            tmp = queue.pop()
            left = tmp.left
            right =tmp.right
            tmp.left = right
            tmp.right = left
            if left:
                queue.insert(0, left)
            if right:
                queue.insert(0, right)
        return root

    def print_tree(self, root, level=0):
        if root is None:
            return
        print("  " * level + str(root.val))
        self.print_tree(root.left, level+1)
        self.print_tree(root.right, level+1)
