class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        
        def count_islands():
            seen = set()
            
            def dfs(r, c):
                stack = [(r, c)]
                while stack:
                    x, y = stack.pop()
                    for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1 and (nx, ny) not in seen:
                            seen.add((nx, ny))
                            stack.append((nx, ny))
            
            islands = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1 and (i, j) not in seen:
                        islands += 1
                        seen.add((i, j))
                        dfs(i, j)
            return islands
        
        if count_islands() != 1:
            return 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands() != 1:
                        return 1
                    grid[i][j] = 1
        
        return 2

    def minDaysToDisconnect(grid):
        if not grid:
            return 0

        original_islands = numIslands([row[:] for row in grid])

        if original_islands > 1:
            return 0  # Already disconnected

        min_changes = float('inf')
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    # Change this cell to water and check islands
                    grid[i][j] = '0'
                    if numIslands([row[:] for row in grid]) > 1:
                        min_changes = min(min_changes, 1)
                    # Restore cell
                    grid[i][j] = '1'

        # If single cell change is not sufficient, check for 2 changes
        if min_changes == float('inf'):
            return 2

        return min_changes