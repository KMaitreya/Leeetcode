class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:

        # expected=['B', 'W', 'W', 'W']

        # print(sorted(grid[0][0]+grid[0][1]+grid[1][0]+grid[1][1]), sorted(grid[0][1]+grid[0][2]+grid[1][2]+grid[1][2]), sorted(grid[1][0]+grid[1][1]+grid[2][0]+grid[2][1]),sorted(grid[1][1]+grid[1][2]+grid[2][1]+grid[2][2]))
        
        # if sorted(grid[0][0]+grid[0][1]+grid[1][0]+grid[1][1])==expected:
        #     return True

        # if sorted(grid[0][1]+grid[0][2]+grid[1][1]+grid[1][2])==expected:
        #     return True

        # if sorted(grid[1][0]+grid[1][1]+grid[2][0]+grid[2][1])==expected:
        #     return True

        # if sorted(grid[1][1]+grid[1][2]+grid[2][1]+grid[2][2])==expected:
        #     return True

        # return False

        def helper(section):

            w, b=0, 0
            
            for cell in section:
                if cell=='W':
                    w+=1
                else:
                    b+=1

            return b in [0, 1] or w in [0, 1]

        sections=[[grid[0][0], grid[0][1], grid[1][0], grid[1][1]], [grid[0][1], grid[0][2], grid[1][1], grid[1][2]], [grid[1][0], grid[1][1], grid[2][0], grid[2][1]], [grid[1][1], grid[1][2], grid[2][1], grid[2][2]]]

        for section in sections:
            if helper(section):
                return True
        
        return False
