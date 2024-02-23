from typing import List, Optional
import unittest

class TreeNode:
    def __init__(self, val = 0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        l = len(nums)
        if not nums:
            return None
        mid_node = l // 2

        root = TreeNode(nums[mid_node])
        root.left = self.sortedArrayToBST(nums[:mid_node])
        root.right = self.sortedArrayToBST(nums[mid_node + 1:])
        return root
        # return TreeNode(
        #     nums[mid_node],
        #     self.sortedArrayToBST(nums[:mid_node]),
        #     self.sortedArrayToBST(nums[mid_node + 1:])
        #     )

# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#         def helper(l, r):
#             if l <= r:
#                 midnode = (r + l) // 2
#                 root = TreeNode(nums[midnode])
#                 root.left = helper(l, midnode-1)
#                 root.right = helper(midnode+1, r)
#                 return root
#         return helper(0, len(nums)-1)

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_sortedArrayToBST(self):
        nums = [-10, -3, 0, 5, 9]
        root = self.solution.sortedArrayToBST(nums)

        # Validate root
        self.assertEqual(root.val, 0)

        # Validate left subtree
        self.assertEqual(root.left.val, -3)
        self.assertEqual(root.left.left.val, -10)
        self.assertIsNone(root.left.right)

        # Validate right subtree
        self.assertEqual(root.right.val, 9)
        self.assertEqual(root.right.left.val, 5)
        self.assertIsNone(root.right.right)

