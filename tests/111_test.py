from typing import List, Optional
from collections import deque
import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([(root, 1)])
        while q:
            node, d = q.popleft()

            if node.left is None and node.right is None:
                return d
            if node.left:
                q.append((node.left, d + 1))
            if node.right:
                q.append((node.right, d + 1))

class TestSolution(unittest.TestCase):
    def test_minDepth(self):
        # Подготовка дерева
        #       3
        #      / \
        #     9   20
        #         / \
        #        15  7
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        solution = Solution()
        self.assertEqual(solution.minDepth(root), 2)
