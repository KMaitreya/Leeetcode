class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        def isMagic(a, b, c, d, e, f, g, h, i):
            return (sorted([a, b, c, d, e, f, g, h, i]) == list(range(1, 10)) and
                    (a + b + c == d + e + f == g + h + i ==  # rows
                    a + d + g == b + e + h == c + f + i ==  # columns
                    a + e + i == c + e + g))  # diagonals

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for i in range(rows - 2):
            for j in range(cols - 2):
                if grid[i+1][j+1] != 5:  # The center of a 3x3 magic square is always 5
                    continue
                if isMagic(grid[i][j], grid[i][j+1], grid[i][j+2],
                        grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
                        grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]):
                    count += 1

        return count