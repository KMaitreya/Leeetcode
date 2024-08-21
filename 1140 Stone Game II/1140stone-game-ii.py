class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        n = len(piles)
        # total_sum[i] will store the total number of stones from pile i to the end
        total_sum = [0] * (n + 1)
        
        # Initialize total_sum
        for i in range(n - 1, -1, -1):
            total_sum[i] = total_sum[i + 1] + piles[i]
        
        # dp[i][m] will store the maximum number of stones Alice can get
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Compute dp array
        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                for x in range(1, 2 * m + 1):
                    if i + x > n:
                        break
                    dp[i][m] = max(dp[i][m], total_sum[i] - dp[i + x][max(m, x)])
        
        # The answer is the maximum number of stones Alice can get starting from pile 0 with M = 1
        return dp[0][1]