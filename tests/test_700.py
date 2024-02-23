from typing import Optional
import unittest

class TreeNode:
    def __init__(self, left=None, right=None, val=0):
        self.left = left
        self.right = right
        self.val = val

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if not root: return None
        # if root.val == val: return root
        # if val < root.val:
        #     return self.searchBST(root.left, val)
        # if val > root.val:
        #     return self.searchBST(root.right, val)
        node = root
        while node:
            if node.val == val: return node
            if node.val < val:
                node = node.right
            else:
                node = node.left
        return None



class TestSolution(unittest.TestCase):
    def test_searchBST(self):
        # Create a binary search tree
        #       4
        #      / \
        #     2   7
        #    / \
        #   1   3
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)

        solution = Solution()

        # Test cases
        self.assertEqual(solution.searchBST(root, 2), root.left)
        self.assertEqual(solution.searchBST(root, 5), None)
        self.assertEqual(solution.searchBST(root, 1), root.left.left)
        self.assertEqual(solution.searchBST(root, 7), root.right)
        self.assertEqual(solution.searchBST(root, 3), root.left.right)
        self.assertEqual(solution.searchBST(root, 8), None)
