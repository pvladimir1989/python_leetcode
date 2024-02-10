import pytest

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        s = set(nums)
        for val in range(len(nums) + 1):
            if val not in s:
                return val


@pytest.mark.parametrize("array, expected",
    [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8)
    ])
def test_missingNumber(array, expected):
    solution = Solution()
    assert solution.missingNumber(array) == expected
