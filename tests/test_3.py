import pytest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        memory, l, r = set(), 0, 0
        for r, ch in enumerate(s):
            while ch in memory:
                left_ch = s[l]
                memory.remove(left_ch)
                l += 1 
            memory.add(ch)
            res = max(r - l + 1, res)    
        return res
    
@pytest.mark.parametrize("s, expected", [
    ("abcabcbb", 3)
])
def test_lengthOfLongestSubstring(s, expected):
    solution = Solution()
    assert solution.lengthOfLongestSubstring(s) == expected



