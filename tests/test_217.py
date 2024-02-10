import pytest

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False
        # return len(set(nums)) != len(nums)

@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 1], True),         # Duplicates present
    ([4, 5, 6, 7], False),         # No duplicates
    ([8, 9, 10, 11, 11], True),    # Duplicates present at the end
    ([], False),                   # Empty list
    ([42], False),                 # Single element list
    ([1, 2, 3, 4, 5, 2], True),    # Duplicates present in the middle
])
def test_containsDuplicate(nums, expected):
    solution = Solution()
    assert solution.containsDuplicate(nums) == expected
