class Solution:
    def tribonacci(self, n: int) -> int:

        dp = defaultdict(int)
        def dfs(n):
            if n == 0:
                dp[n]

            if n == 1 or n==2:
                return 1

            if n in dp:
                return dp[n]

            dp[n] = dfs(n-1)+dfs(n-2)+dfs(n-3)

            return dp[n]
        
            

        return dfs(n)