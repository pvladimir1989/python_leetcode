import pytest
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         d1 = {}
#         d2 = {}
#         i = 1
#         for ss in s:
#             if ss in d1:
#                 d1[ss] += i
#                 continue
#             d1[ss] = 1
#         for tt in t:
#             if tt in d2:
#                 d2[tt] += i
#                 continue
#             d2[tt] = 1
#         return d1 == d2



@pytest.mark.parametrize("w1, w2, expected", [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
])
def test_isAnagram(w1, w2, expected):
    solution = Solution()
    assert solution.isAnagram(w1, w2) == expected
