import pytest

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        l = []
        s1 = set(nums)
        for i in range(1, len(nums)+1):
            if i not in s1:
                l.append(i)
        return l

@pytest.mark.parametrize("array, expected", [
    ([4,3,2,7,8,2,3,1], [5,6]),
    ([1,1], [2]),
])
def test_findDisappearedNumbers(array, expected):
    solution = Solution()
    assert solution.findDisappearedNumbers(array) == expected
