import collections
import pytest


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        memory, res, left = collections.defaultdict(int), 0, 0
        for right, ch in enumerate(s):
            memory[ch] += 1
            if right - left == 3:
                l = s[left]
                memory[l] -= 1
                if memory[l] == 0:
                    del memory[l]
                left += 1
            if len(memory) == 3:
                res += 1
        return res


@pytest.mark.parametrize(
    "s, expected",
    [
        ("xyzzaz", 1),
    ],
)
def test_countGoodSubstrings(s, expected):
    solution = Solution()
    assert solution.countGoodSubstrings(s) == expected
