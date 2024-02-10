import pytest
from collections import defaultdict

class Solution:
    def longestSubstringwithAtMostTwo(self, s: str, k: int) -> int:
        res = 0
        mem, l, r = defaultdict(int), 0, 0
        for r, ch in enumerate(s):
            mem[ch] += 1
            while len(mem) > k:
                left_ch = s[l]
                mem[left_ch] -= 1
                if mem[left_ch] == 0: del mem[left_ch]
                l += 1
            res = max(r - l + 1, res)
        return res

@pytest.mark.parametrize("s, k, expected", [
    ("eceba", 3, 4)
])
def test_longestSubstringwithAtMostTwo(s, k, expected):
    solution = Solution()
    assert solution.longestSubstringwithAtMostTwo(s, k) == expected