from typing import List, Optional
import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2: return None
        if not root1: return root2
        if not root2: return root1

        root = TreeNode(root1.val + root2.val)
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)

        return root


class TestSolution(unittest.TestCase):
    def test_mergeTrees(self):
        solution = Solution()

        # Test Case 1
        # Constructing tree 1
        #     1
        #    / \
        #   3   2
        #  /       \
        # 5         4
        root1 = TreeNode(1)
        root1.left = TreeNode(3)
        root1.right = TreeNode(2)
        root1.left.left = TreeNode(5)

        # Constructing tree 2
        #     2
        #    / \
        #   1   3
        #    \   \
        #     4   7
        root2 = TreeNode(2)
        root2.left = TreeNode(1)
        root2.right = TreeNode(3)
        root2.left.right = TreeNode(4)
        root2.right.right = TreeNode(7)

        # Merging trees
        #     3
        #    / \
        #   4   5
        #  / \   \
        # 5   4   7
        merged_tree = solution.mergeTrees(root1, root2)
        self.assertEqual(merged_tree.val, 3)
        self.assertEqual(merged_tree.left.val, 4)
        self.assertEqual(merged_tree.right.val, 5)
        self.assertEqual(merged_tree.left.left.val, 5)
        self.assertEqual(merged_tree.left.right.val, 4)
        self.assertEqual(merged_tree.right.right.val, 7)

        # Test Case 2
        # Merging empty trees
        merged_tree = solution.mergeTrees(None, None)
        self.assertIsNone(merged_tree)
