import pytest

class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique = set()
        for email in emails:
            e = email.split("@")[0]
            e1 = email.split("@")[1]
            without_dots = e.replace(".", "")
            without_plus = without_dots.split("+")[0]
            unique.add(f"{without_plus}@{e1}")
        return len(unique)

@pytest.mark.parametrize("emails, expected", [
    (["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"], 2),
    (["a@leetcode.com","b@leetcode.com", "c@leetcode.com"], 3),
])
def test_numUniqueEmails(emails, expected):
    solution = Solution()
    assert solution.numUniqueEmails(emails) == expected
