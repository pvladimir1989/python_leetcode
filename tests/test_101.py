from typing import Optional
import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def is_mirror(left, right):
            if not left and not right:
                return True

            if not left or not right or left.val != right.val:
                return False

            return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

        return is_mirror(root, root)


class TestSolution(unittest.TestCase):
    def test_isSymmetric(self):
        solution = Solution()

        # Test case 1: Symmetric tree
        #     1
        #    / \
        #   2   2
        #  / \ / \
        # 3  4 4  3
        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(2)
        root1.left.left = TreeNode(3)
        root1.left.right = TreeNode(4)
        root1.right.left = TreeNode(4)
        root1.right.right = TreeNode(3)
        self.assertTrue(solution.isSymmetric(root1))

        # Test case 2: Asymmetric tree
        #     1
        #    / \
        #   2   2
        #    \   \
        #    3    3
        root2 = TreeNode(1)
        root2.left = TreeNode(2)
        root2.right = TreeNode(2)
        root2.left.right = TreeNode(3)
        root2.right.right = TreeNode(3)
        self.assertFalse(solution.isSymmetric(root2))

        # Test case 3: Edge case with an empty tree
        root3 = None
        self.assertTrue(solution.isSymmetric(root3))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = [root.left, root.right]
        while stack:
            node1, node2 = stack.pop(), stack.pop()
            if node1 is None and node2 is None: continue
            elif (node1 is None or node2 is None) or node1.val != node2.val:
                return False

            stack.append(node1.left)
            stack.append(node2.right)
            stack.append(node1.right)
            stack.append(node2.left)
        return True


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         stack = [root.left, root.right]
#         while stack:
#             node1,node2 = stack.pop(), stack.pop()
#             if node1 is None and node2 is None: continue
#             elif (node1 is None or node2 is None) or node1.val != node2.val:
#                 return False

#             stack.append(node1.left)
#             stack.append(node2.right)
#             stack.append(node1.right)
#             stack.append(node2.left)
#         return True
