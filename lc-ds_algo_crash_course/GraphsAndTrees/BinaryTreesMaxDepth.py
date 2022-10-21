"""
Given the root of a binary tree,
find the maximum depth - the number of nodes along the longest path from the root to a leaf.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def max_depth(root: TreeNode) -> int:
    if not root:
        return 0

    left = max_depth(root.left)
    right = max_depth(root.right)
    return max(left, right) + 1


# pre-order traversal
def maxDepth(root: [TreeNode]) -> int:
    if not root:
        return 0

    stack = [(root, 1)]
    ans = 0

    while stack:
        node, depth = stack.pop()
        ans = max(ans, depth)
        if node.left:
            stack.append((node.left, depth + 1))
        if node.right:
            stack.append((node.right, depth + 1))

    return ans
