import pytest

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return list(set(t)-set(s))[0]


@pytest.mark.parametrize("t, s, expected", [
    ("abcd", "abcde", "e"),
    ("", "y", "y"),
])
def test_findTheDifference(t, s, expected):
    solution = Solution()
    assert solution.findTheDifference(t, s) == expected
