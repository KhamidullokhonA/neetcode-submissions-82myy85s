class Solution:

    def tribonacci(self, n: int) -> int:
        dp = {}

        def helper(n):
            if n in dp:
                return dp[n]

            if n == 0:
                return 0
            if n==1 or n==2:
                return 1
            dp[n] = helper(n-1)+helper(n-2)+helper(n-3)
            return dp[n]

        return helper(n)