class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        
        hmap={}

        for row in matrix:
            if row[0]==1:
                row=[bit^1 for bit in row]

            hmap[tuple(row)]=1+hmap.get(tuple(row), 0)

        return max(hmap.values())
