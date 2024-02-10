import pytest
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l <= r:
            sum_numbers = numbers[l] + numbers[r]
            if sum_numbers > target:
                r -= 1
            elif sum_numbers < target:
                l += 1
            else:
                return [l + 1, r + 1]


@pytest.mark.parametrize("nums, target, expected", [([2, 7, 11, 15], 9, [1, 2])])
def test_twoSum(nums, target, expected):
    solution = Solution()
    assert solution.twoSum(nums, target) == expected
