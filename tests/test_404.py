from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        stack = [(root, None)]
        while stack:
            cur, is_left = stack.pop()
            if not cur.left and not cur.right and is_left == True:
                ans += cur.val
            if cur.left:
                stack.append((cur.left,1))
            if cur.right:
                stack.append((cur.right,0))
        return ans


def test_sumOfLeftLeaves():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()
    assert solution.sumOfLeftLeaves(root) == 24, "Test case 1 failed"
