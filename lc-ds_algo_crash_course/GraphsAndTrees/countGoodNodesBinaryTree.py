"""
Given a binary tree root, a node X in the tree is named good
if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_good_nodes(root: TreeNode) -> int:
    def count_nodes_dfs(node, val):
        if not node:
            return 0

        left = count_nodes_dfs(node.left, max(val, node.val))
        right = count_nodes_dfs(node.right, max(val, node.val))

        ans = left + right

        if node.val >= val:
            ans += 1

        return ans

    return count_nodes_dfs(root, float("-inf"))




