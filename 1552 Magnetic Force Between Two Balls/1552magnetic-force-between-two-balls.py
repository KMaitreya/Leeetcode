class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
    
        def canPlaceBalls(min_force):
            # Place the first ball in the first basket
            count = 1
            last_position = position[0]
            
            # Try to place the remaining balls
            for i in range(1, len(position)):
                if position[i] - last_position >= min_force:
                    count += 1
                    last_position = position[i]
                if count == m:
                    return True
            
            return False
        
        low, high = 1, position[-1] - position[0]
        best = 0
        
        while low <= high:
            mid = (low + high) // 2
            if canPlaceBalls(mid):
                best = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return best