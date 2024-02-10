import pytest


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        d = {}
        l = len(nums) // 2
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        for k in d:
            if d[k] > l:
                return k
            else:
                continue

@pytest.mark.parametrize("nums, expected",
    [
        ([3,2,3], 3),
        ([2,2,1,1,1,2,2], 2)
    ])
def test_majorityElement(nums, expected):
    solution = Solution()
    assert solution.majorityElement(nums) == expected
