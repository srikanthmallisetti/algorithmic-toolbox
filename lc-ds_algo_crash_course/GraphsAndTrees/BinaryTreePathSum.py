"""
Given the root of a binary tree and an integer targetSum,
return true if there is a path from the root to a leaf such that the sum of the nodes on the path is equal to targetSum,
and return false otherwise.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def target_sum(root: TreeNode, target: int) -> bool:
    def dfs(node: TreeNode, curr: int) -> bool:

        if not node:
            return False

        if node.right is None and node.left is None:
            return (curr + node.val) == target

        curr += node.val
        left = dfs(node.left, curr)
        right = dfs(node.right, curr)

        return left or right

    return dfs(root, 0)
