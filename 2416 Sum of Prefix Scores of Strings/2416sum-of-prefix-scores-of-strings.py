class Solution:
    from collections import defaultdict
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        prefix_count = defaultdict(int)
    
        # First, populate the prefix_count dictionary
        for word in words:
            prefix = ""
            for char in word:
                prefix += char
                prefix_count[prefix] += 1
        
        # Now calculate the score for each word
        result = []
        for word in words:
            prefix = ""
            total_score = 0
            for char in word:
                prefix += char
                total_score += prefix_count[prefix]
            result.append(total_score)
        
        return result
