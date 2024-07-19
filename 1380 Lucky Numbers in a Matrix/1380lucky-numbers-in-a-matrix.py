class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        matrixt=[list(row) for row in zip(*matrix)]

        mins, maxst=[], []

        for row in matrix:
            mins.append(min(row))

        for row in matrixt:
            maxst.append(max(row))

        return set(mins) & set(maxst)