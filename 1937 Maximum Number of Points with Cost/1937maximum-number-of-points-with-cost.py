class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        m, n = len(points), len(points[0])
    
        # Initialize dp with the first row
        dp = points[0][:]
        
        for r in range(1, m):
            new_dp = [0] * n
            
            # Compute left and right max arrays
            left = [0] * n
            left[0] = dp[0]
            for c in range(1, n):
                left[c] = max(left[c-1], dp[c] + c)
            
            right = [0] * n
            right[n-1] = dp[n-1] - (n-1)
            for c in range(n-2, -1, -1):
                right[c] = max(right[c+1], dp[c] - c)
            
            # Calculate new dp values
            for c in range(n):
                new_dp[c] = points[r][c] + max(left[c] - c, right[c] + c)
            
            dp = new_dp
        
        return max(dp)