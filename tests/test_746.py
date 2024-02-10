from typing import List
import pytest

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n+1)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

        return min(dp[n-1], dp[n-2])


@pytest.mark.parametrize("n, expected", [
    ([10,15,20], 15),
    ([1,100,1,1,1,100,1,1,100,1], 6)
])
def test_minCostClimbingStairs(n, expected):
    solution = Solution()
    assert solution.minCostClimbingStairs(n) == expected
