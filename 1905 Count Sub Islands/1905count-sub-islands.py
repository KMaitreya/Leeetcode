class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        def dfs(i, j):
            if i < 0 or i >= len(grid1) or j < 0 or j >= len(grid1[0]) or grid2[i][j] == 0:
                return True
            
            # If the current cell in grid2 is part of an island but not in grid1, this cannot be a sub-island
            if grid1[i][j] == 0:
                return False

            # Mark the cell as visited by setting it to 0
            grid2[i][j] = 0

            # Check all four directions
            up = dfs(i - 1, j)
            down = dfs(i + 1, j)
            left = dfs(i, j - 1)
            right = dfs(i, j + 1)

            # Return True if all parts of the island in grid2 are also in grid1
            return up and down and left and right

        sub_islands = 0
        
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:  # Found an island in grid2
                    # Perform DFS and check if it's a sub-island
                    if dfs(i, j):
                        sub_islands += 1

        return sub_islands
