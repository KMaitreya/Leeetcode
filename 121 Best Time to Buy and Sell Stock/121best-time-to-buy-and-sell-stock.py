class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l=0
        m=0

        for r in range(1, len(prices)):
            if prices[l]<prices[r]:
                if m<prices[r]-prices[l]:
                    m=prices[r]-prices[l]
            else:
                l=r

        return m

