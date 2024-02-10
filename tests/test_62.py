import pytest


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]

        # O(n * m) O(n)
@pytest.mark.parametrize("r, c, expected", [
    (3, 7, 28)
])
def test_uniquePaths(r, c, expected):
    solution = Solution()
    assert solution.uniquePaths(r, c,) == expected
