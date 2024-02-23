from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()
        stack = [root]
        while stack:
            cur = stack.pop()
            if k - cur.val in s:
                return True
            s.add(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return False

import unittest

class TestSolution(unittest.TestCase):
    def test_findTarget(self):
        # Create a tree:      5
        #                    / \
        #                   3   6
        #                  / \   \
        #                 2   4   7
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(6)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.right.right = TreeNode(7)

        solution = Solution()
        self.assertTrue(solution.findTarget(root, 9))  # 2 + 7 = 9
        self.assertTrue(solution.findTarget(root, 6))  # 2 + 4 = 6
        self.assertFalse(solution.findTarget(root, 10))  # No pair adds up to 10

    def test_findTarget_empty(self):
        # Test with an empty tree
        solution = Solution()
        self.assertFalse(solution.findTarget(None, 5))
