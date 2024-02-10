import pytest
from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        def get_palindrome(s:str, l: str, r: str) -> str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r] 
        
        for i in range(len(s)):
            p1, p2 = get_palindrome(s, i, i), get_palindrome(s, i, i + 1)
            if len(p1) > len(res):
                res = p1
            if len(p2) > len(res):
                res = p2
            
        return res
    
@pytest.mark.parametrize("s, expected", [
    ("babad", "bab")
])
def test_longestPalindrome(s, expected):
    solution = Solution()
    assert solution.longestPalindrome(s) == expected