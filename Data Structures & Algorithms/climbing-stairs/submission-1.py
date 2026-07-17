class Solution:
    
    def climbStairs(self, n: int) -> int:
        dp = {}

        def fib(n):
            if n in dp:
                return dp[n]

            if n==1:
                return 1
            if n==2:
                return 2
            if n==3:
                return 3

            dp[n] = fib(n-1)+fib(n-2)

            return dp[n]
        return fib(n)