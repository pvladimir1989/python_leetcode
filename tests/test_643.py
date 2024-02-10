import pytest
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = 0
        for i in range(k):
            s += nums[i]
        max_sum = s
        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]
            max_sum = max(max_sum, s)
        return max_sum / k


@pytest.mark.parametrize(
    "lst, k, exp",
    [
        ([1, 12, -5, -6, 50, 3], 4, 12.75000),
        # Add more test cases as needed
    ],
)
def test_findMaxAverage(lst, k, exp):
    solution = Solution()
    max_av = solution.findMaxAverage(lst, k)
    assert max_av == exp
