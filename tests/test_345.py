import pytest


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u"}
        lst = list(s)
        l, r = 0, len(lst) - 1
        while l <= r:
            if not lst[l].lower() in vowels:
                l += 1
                continue
            if not lst[r].lower() in vowels:
                r -= 1
                continue
            lst[l], lst[r] = lst[r], lst[l]
            l += 1
            r -= 1
        return "".join(lst)


@pytest.mark.parametrize(
    "s, expected",
    [("hello", "holle")],
)
def test_reverseVowels(s, expected):
    solution = Solution()
    assert solution.reverseVowels(s) == expected
