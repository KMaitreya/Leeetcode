class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        remainder_counts = Counter(x % k for x in arr)
    
        for r in remainder_counts:
            if r == 0:  # Special case for remainder 0
                if remainder_counts[r] % 2 != 0:
                    return False
            else:
                complement = (k - r) % k
                if remainder_counts[r] != remainder_counts[complement]:
                    return False
        
        return True
                
