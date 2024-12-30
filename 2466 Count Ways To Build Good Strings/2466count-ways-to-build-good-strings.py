class Solution:
    # def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
    #     res=0
    #     def pascal(rowIndex):
    #         row = [1]
    #         for _ in range(rowIndex):
    #             row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]
    #         return row

    #     for num in range(low, high+1):
    #         row=pascal(num)
    #         l=len(row) 
    #         start=max(0, zero-1)
    #         end=min(l, l-one+1)
    #         res+=sum(row[start:end])

    #     return res%(10**9+7)

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7

        # Initialize DP array
        dp = [0] * (high + 1)
        dp[0] = 1  # Base case: One way to form a string of length 0

        # Fill the DP array
        for i in range(1, high + 1):
            if i >= zero:
                dp[i] += dp[i - zero]
            if i >= one:
                dp[i] += dp[i - one]
            dp[i] %= MOD

        # Sum up all valid lengths
        result = 0
        for i in range(low, high + 1):
            result += dp[i]
            result %= MOD

        return result

