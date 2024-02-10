import pytest
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros, l, res = 0, 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                while zeros >= k:
                    if nums[l] == 0:
                        zeros -= 1
                    l += 1
                zeros += 1
            res = max(right - l + 1, res)
        return res
    
@pytest.mark.parametrize("nums, k, expected", [
    ([1,1,1,0,0,0,1,1,1,1,0], 2, 6)
])
def test_longestOnes(nums, k, expected):
    solution = Solution()
    assert solution.longestOnes(nums, k) == expected