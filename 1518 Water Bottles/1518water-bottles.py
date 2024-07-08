class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        bottle=numBottles

        while numBottles>=numExchange:
            nb=numBottles//numExchange
            bottle+=nb
            numBottles=nb+numBottles%numExchange
            

        return bottle

        