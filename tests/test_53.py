from typing import List
import pytest

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n)
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        return max(dp)

@pytest.mark.parametrize("lst, expected", [
    ([-2,1,-3,4,-1,2,1,-5,4], 6)
])
def test_maxSubArray(lst, expected):
    solution = Solution()
    assert solution.maxSubArray(lst) == expected
