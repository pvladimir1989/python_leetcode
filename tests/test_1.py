import pytest


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i, val in enumerate(nums):
            if target - val in d:
                return [d[target - val], i]
            else:
                d[val] = i

@pytest.mark.parametrize("array, target, expected", [
    ([2,7,11,15], 9, [0,1]),
    ([3,2,4], 6, [1,2]),
])
def test_twoSum(array, target, expected):
    solution = Solution()
    assert solution.twoSum(array, target) == expected
