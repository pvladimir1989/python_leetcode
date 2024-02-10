import pytest

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
        for i, val in enumerate(s):
            if val in d and d[val] == 1:
                return i
            else:
                continue
        return -1


@pytest.mark.parametrize("s, expected",
    [
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("aabb", -1)
    ])
def test_intersection(s, expected):
    solution = Solution()
    assert solution.firstUniqChar(s) == expected
