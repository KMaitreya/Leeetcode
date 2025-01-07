class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        
        for i in range(1, len(grid[0])):
            if grid[0][i-1]==grid[0][i]:
                return False

        for i in range(1, len(grid)):
            if grid[i-1]!=grid[i]:
                return False

        return True