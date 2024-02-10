import pytest
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        i = 0
        while i < len(arr) - 1 and arr[i] < arr[i + 1]:
            i += 1

        j = len(arr) - 1
        while j > 0 and arr[j] < arr[j - 1]:
            j -= 1

        return i == j and 0 < i < len(arr) - 1


@pytest.mark.parametrize("lst, expected", [([2, 1], False)])
def test_validMountainArray(lst, expected):
    solution = Solution()
    assert solution.validMountainArray(lst) == expected
