import pytest

# class Solution:
#     def fib(self, n: int) -> int:
#         return self.f(n)

#     def f(self, n):
#         if n <= 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             return self.fib(n-1) + self.fib(n-2)

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return n
        if n == 1:
            return n

        f0 = 0
        f1 = 1
        while n > 1:
            f1, f0 = f1 + f0, f1
            n -= 1
        return f1

@pytest.mark.parametrize("n, exp" ,[
    (2, 1),
    (3, 2),
    (5, 5),
    (6, 8)
    # Add more test cases as needed
])
def test_fib(n, exp):
    solution = Solution()
    fib = solution.fib(n)
    assert fib == exp
