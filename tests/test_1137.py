import pytest


# class Solution:
#     def tribonacci(self, n: int) -> int:
#         lst = [0, 1, 1]
#         if 3 > n:
#             return lst[n]
#         for i in range(3, n - 1):
#             lst.append(lst[i-3] + lst[i-2] + lst[i-1])
#         return lst[-1]

class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0:
            return 0

        if n ==1 or n == 2:
            return 1

        t0, t1, t2 = 0, 1, 1

        while n > 2:
            t2, t1, t0 = t2+t1+t0, t2, t1
            n -= 1

        return t2

@pytest.mark.parametrize("n, expected", [
    (4, 4),
    (25, 1389537)
])
def test_tribonacci(n, expected):
    solution = Solution()
    assert solution.tribonacci(n) == expected
