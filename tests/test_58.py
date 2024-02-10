import pytest


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # return len(s.split(" ")[-1])??

        word = ""
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                if word:
                    return len(word)
            else:
                word += s[i]
        return len(word)


@pytest.mark.parametrize("s, expected", [("   fly me   to   the moon  ", 4)])
def test_lengthOfLastWord(s, expected):
    solution = Solution()
    assert solution.lengthOfLastWord(s) == expected
