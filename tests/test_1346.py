import pytest

class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        seen = set()
        for a in arr:
            if a * 2 in seen or a % 2 == 0 and a // 2 in seen:
                return True
            seen.add(a)
        return False


@pytest.mark.parametrize("array, expected", [
    ([10,2,5,3], True),
    ([3,1,7,11], False),
])
def test_checkIfExist(array, expected):
    solution = Solution()
    assert solution.checkIfExist(array) == expected
