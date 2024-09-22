class Solution:
    
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(n, curr, next):
            steps = 0
            while curr <= n:
                steps += min(n + 1, next) - curr
                curr *= 10
                next *= 10
            return steps
        current = 1
        k -= 1  # Decrease k by 1 to handle zero-indexing

        while k > 0:
            steps = count_steps(n, current, current + 1)
            if steps <= k:
                # If the steps are less than or equal to k, skip this subtree
                k -= steps
                current += 1
            else:
                # Move down to the next level (deeper in lexicographical order)
                current *= 10
                k -= 1

        return current