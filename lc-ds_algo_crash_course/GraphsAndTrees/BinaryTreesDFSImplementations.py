"""
BST DFS Traversal - Pre-order, In-order, Post-order
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def dfs_preorder(node):
    if not node:
        return

    print(node.val)
    dfs_preorder(node.left)
    dfs_preorder(node.right)


def dfs_inorder(node):
    if not node:
        return

    dfs_preorder(node.left)
    print(node.val)
    dfs_preorder(node.right)


def dfs_postorder(node):
    if not node:
        return

    dfs_preorder(node.left)
    dfs_preorder(node.right)
    print(node.val)
