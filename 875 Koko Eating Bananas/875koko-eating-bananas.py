class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        ## TRY BRUTEFORCE SOLUTION

        ### BINARY SEARCH

        def check(k):
            hr=0
            for pile in piles:
                hr+=math.ceil(pile/k)
            return hr

        l, r=1, max(piles)
        res=r

        while l<=r:
            k=(l+r)//2
            if check(k)<=h:
                res=min(res, k)
                r=k-1
            else:
                l=k+1

        return res


            
                

        