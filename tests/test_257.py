from typing import Optional, List
import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []

        def dfs(node, path):
            path += str(node.val) + "->"

            if not node.left and not node.right:
                ans.append(path[:-2])
                return

            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)
        dfs(root,"")

        return ans

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_binaryTreePaths(self):
        # Create a binary tree
        #      1
        #     / \
        #    2   3
        #     \
        #      5
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)

        expected_output = ["1->2->5", "1->3"]
        self.assertEqual(self.solution.binaryTreePaths(root), expected_output)
