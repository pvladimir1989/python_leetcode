import pytest


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l, r = 1, x // 2
        while l <= r:
            mid = (l + r) // 2
            target = mid * mid
            if target == x:
                return mid
            if target < x:
                l = mid + 1
            else:
                r = mid - 1
        return r


@pytest.mark.parametrize("n, expected", [(8, 2)])
def test_mySqrt(n, expected):
    solution = Solution()
    assert solution.mySqrt(n) == expected
