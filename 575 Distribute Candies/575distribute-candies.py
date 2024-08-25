class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        c1=len(set(candyType))
        c2=len(candyType)/2

        if c1<c2:
            return c1
        return int(c2)