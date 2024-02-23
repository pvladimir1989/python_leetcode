from typing import Optional
import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return max(l, r) + 1


class TestSolution(unittest.TestCase):
    def test_maxDepth(self):
        # Create a tree:      3
        #                    / \
        #                   9  20
        #                     /  \
        #                    15   7
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        solution = Solution()
        self.assertEqual(solution.maxDepth(root), 3)

    def test_maxDepth_empty(self):
        # Test with an empty tree
        solution = Solution()
        self.assertEqual(solution.maxDepth(None), 0)
