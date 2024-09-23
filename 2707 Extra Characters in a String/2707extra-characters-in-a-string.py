class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        word_set = set(dictionary)
    
        # Initialize the dp array with large values (infinity) since we are minimizing
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Base case: no extra characters for an empty string
        
        # Loop through each character position i in s
        for i in range(1, n + 1):
            # By default, the extra character is added if no match is found
            dp[i] = dp[i - 1] + 1
            
            # Check every possible start position j
            for j in range(i):
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])
        
        return dp[n]
                